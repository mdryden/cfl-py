from __future__ import annotations

from typing import List, Optional

from cflpy.models.team_leaders import defence
from cflpy.proxy import Proxy


class DefenceClient:
    def __init__(self, proxy: Proxy, season: int):
        assert season, "season must be provided"
        self.proxy = proxy
        self.season = season

    def get_passing(self) -> Optional[List[defence.Passing]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/defence/category/passing"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [defence.Passing(**x) for x in data]

    def get_rushing(self) -> Optional[List[defence.Rushing]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/defence/category/rushing"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [defence.Rushing(**x) for x in data]

    def get_receiving(self) -> Optional[List[defence.Receiving]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/defence/category/receiving"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [defence.Receiving(**x) for x in data]

    def get_tackles(self) -> Optional[List[defence.Tackles]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/defence/category/tackles"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [defence.Tackles(**x) for x in data]
