import time
from typing import Callable, Dict, List, Optional

import requests
from ratelimiter import RateLimiter

from cflpy.exceptions import ApiException


class Proxy:
    def __init__(
        self,
        api_key: str,
        endpoint: str = "https://api.cfl.ca/v1",
        logging_callback: Callable[[str], None] = None,
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.logging_callback = logging_callback
        self.last_url: Optional[str] = None

    def get(self, path: str) -> List[dict] | dict:

        if not self.api_key:
            msg = (
                "CFL API Key is not set. To enable CFL API requests, please add CFL_API_KEY=<key> to your .env file."
                "You must have a key provided by the CFL; see https://api.cfl.ca/ for more information."
            )
            raise ApiException(msg)

        url = f"{self.endpoint}/{path}"
        url_no_key = url
        self.last_url = url_no_key

        if "?" in url:
            url += f"&key={self.api_key}"
        else:
            url += f"?key={self.api_key}"

        def _log(message: str) -> None:
            if self.logging_callback:
                self.logging_callback(message)

        def _limited(until: float) -> None:
            duration = int(round(until - time.time()))
            _log(f"Rated limit reached, pausing for {duration} seconds")

        @RateLimiter(max_calls=30, period=60, callback=_limited)
        def _get() -> List[dict] | dict:
            response = requests.get(url)

            if response.ok:
                return response.json()["data"]
            else:
                # manual delay since sometimes in case something is happening asynchronously and we can't prevent hitting the limit
                if is_rate_limit_error(response):
                    pause_for = 60
                    _log(f"Hit CFL's rate limit, pausing for {pause_for} seconds")
                    time.sleep(pause_for)
                    return _get(path)
                raise ApiException(response.text, url=url_no_key)

        return _get()


def is_rate_limit_error(response: requests.Response) -> bool:
    try:
        result: Dict = response.json()
        errors: List = result.get("errors", None)
        if errors:
            error_code = errors[0].get("code", None)
            return error_code == 429
    except BaseException:
        pass

    return False
