from typing import Callable, Optional

from cflpy.client_v1 import ClientV1
from cflpy.client_v1_1 import ClientV1_1
from cflpy.proxy import Proxy


class CflPy:
    proxy_v1: Optional[Proxy] = None
    proxy_v1_1: Optional[Proxy] = None

    @classmethod
    def setup(
        cls,
        api_key: str,
        endpoint_base: str = "https://api.cfl.ca",
        logging_callback: Callable[[str], None] = None,
    ) -> None:
        cls.proxy_v1 = Proxy(
            api_key=api_key,
            endpoint=f"{endpoint_base}/v1",
            logging_callback=logging_callback,
        )

        cls.proxy_v1_1 = Proxy(
            api_key=api_key,
            endpoint=f"{endpoint_base}/v1.1",
            logging_callback=logging_callback,
        )

    @classmethod
    def v1(cls) -> ClientV1:
        assert (
            cls.proxy_v1
        ), "CflPy has not been initialized, call CflPy.setup() before using"
        return ClientV1(cls.proxy_v1)

    @classmethod
    def v1_1(cls) -> ClientV1_1:
        assert (
            cls.proxy_v1_1
        ), "CflPy has not been initialized, call CflPy.setup() before using"
        return ClientV1_1(cls.proxy_v1_1)
