from typing import Optional

from cflpy.clients.games import GamesClient
from cflpy.clients.players import PlayersClient
from cflpy.clients.standings import StandingsClient
from cflpy.proxy import Proxy


class ClientV1:
    def __init__(self, proxy: Proxy):
        self.proxy = proxy

    def games(self, season: Optional[int] = None) -> GamesClient:
        return GamesClient(self.proxy, season)

    def players(self) -> PlayersClient:
        return PlayersClient(self.proxy)

    def standings(self, season: int) -> StandingsClient:
        return StandingsClient(self.proxy, season)
