from __future__ import annotations

from typing import Optional

from cflpy.models.standings import Standings
from cflpy.proxy import Proxy


class StandingsClient:
    def __init__(self, proxy: Proxy, season: int):
        assert season, "season must be provided"
        self.proxy = proxy
        self.season = season

    def get(self) -> Optional[Standings]:
        path = f"standings/{self.season}"

        data = self.proxy.get(path)
        assert isinstance(data, dict), "Unexpected result from CFL API"

        return Standings(**data)
