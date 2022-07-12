from cflpy.clients.team_leaders.team_leaders import TeamLeadersClient
from cflpy.proxy import Proxy


class ClientV1_1:
    def __init__(self, proxy: Proxy):
        self.proxy = proxy

    def team_leaders(self, season: int) -> TeamLeadersClient:
        return TeamLeadersClient(self.proxy, season)
