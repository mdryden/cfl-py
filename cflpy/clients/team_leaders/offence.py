from __future__ import annotations

from typing import List, Optional

from cflpy.models.team_leaders import offence
from cflpy.proxy import Proxy


class OffenceClient:
    def __init__(self, proxy: Proxy, season: int):
        assert season, "season must be provided"
        self.proxy = proxy
        self.season = season

    def get_game_stats(self) -> Optional[List[offence.GameStats]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/offence/category/game_stats"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [offence.GameStats(**x) for x in data]

    def get_passing(self) -> Optional[List[offence.Passing]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/offence/category/passing"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [offence.Passing(**x) for x in data]

    def get_rushing(self) -> Optional[List[offence.Rushing]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/offence/category/rushing"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [offence.Rushing(**x) for x in data]

    def get_receiving(self) -> Optional[List[offence.Receiving]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/offence/category/receiving"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [offence.Receiving(**x) for x in data]

    def get_kicking(self) -> Optional[List[offence.Kicking]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/offence/category/kicking"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [offence.Kicking(**x) for x in data]

    def get_field_goals_converts(self) -> Optional[List[offence.FieldGoalsConverts]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/offence/category/field_goals_converts"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [offence.FieldGoalsConverts(**x) for x in data]

    def get_punting_kickoffs(self) -> Optional[List[offence.PuntingKickoffs]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/offence/category/punting_kickoffs"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [offence.PuntingKickoffs(**x) for x in data]

    def get_punt_kickoff_returns(self) -> Optional[List[offence.PuntKickoffReturns]]:
        """Filters are not currently supported"""
        path = f"team_leaders/{self.season}/offence/category/punt_kickoff_returns"

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return [offence.PuntKickoffReturns(**x) for x in data]
