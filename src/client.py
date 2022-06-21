from typing import Callable, Optional

from src.clients.games import GamesClient

from .proxy import Proxy


class Client:
    proxy: Optional[Proxy] = None

    @classmethod
    def setup(
        cls,
        api_key: str,
        endpoint: str = "https://api.cfl.ca/v1",
        logging_callback: Callable[[str], None] = None,
    ) -> None:
        cls.proxy = Proxy(
            api_key=api_key, endpoint=endpoint, logging_callback=logging_callback
        )

    @classmethod
    def games(cls, season: Optional[int] = None) -> GamesClient:
        assert (
            cls.proxy
        ), "Client has not been initialized, call Client.setup() before using"
        return GamesClient(cls.proxy, season)
