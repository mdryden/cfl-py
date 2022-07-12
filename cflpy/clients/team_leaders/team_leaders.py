from cflpy.clients.team_leaders.defence import DefenceClient
from cflpy.clients.team_leaders.offence import OffenceClient
from cflpy.proxy import Proxy


class TeamLeadersClient:
    def __init__(self, proxy: Proxy, season: int):
        assert season, "season is required"
        self.proxy = proxy
        self.season = season

    def offence(self) -> OffenceClient:
        return OffenceClient(self.proxy, self.season)

    def defence(self) -> DefenceClient:
        return DefenceClient(self.proxy, self.season)
