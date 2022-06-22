from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel

from cflpy.models.game import Game
from cflpy.proxy import Proxy


class GameClient:
    def __init__(self, proxy: Proxy, season: int, game_id: int):
        assert season, "season must be provided"
        assert game_id, "game_id must be provided"
        self.proxy = proxy
        self.season = season
        self.game_id = game_id
        self.__includes: List[str] = []

    def get(self) -> Optional[Game]:
        path = f"games/{self.season}/game/{self.game_id}"

        if self.__includes:
            path = f"{path}?include="

            for include in set(self.__includes):
                path += f"{include},"

            path = path[:-1]  # strip trailing comma

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"

        if len(data) == 0:
            return None
        else:
            return Game(**data[0])

    def with_boxscore(self) -> GameClient:
        self.__includes.append("boxscore")
        return self

    def with_play_by_play(self) -> GameClient:
        self.__includes.append("play_by_play")
        return self

    def with_rosters(self) -> GameClient:
        self.__includes.append("rosters")
        return self

    def with_penalties(self) -> GameClient:
        self.__includes.append("penalties")
        return self

    def with_play_reviews(self) -> GameClient:
        self.__includes.append("play_reviews")
        return self

    def with_all(self) -> GameClient:
        return (
            self.with_boxscore()
            .with_play_by_play()
            .with_rosters()
            .with_penalties()
            .with_play_reviews()
        )


class GamesFilter(BaseModel):
    field: Literal[
        "game_id",
        "date_start",
        "season",
        "week",
        "temperature",
        "attendance",
        "team",
        "team_1",
        "team_2",
        "event_type_id",
    ]

    operator: Literal["eq", "ne", "gt", "lt", "ge", "le", "in"] = "eq"

    value: str | int = ""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GamesFilter):
            return False

        return (
            self.field == other.field
            and self.operator == other.operator
            and self.value == other.value
        )

    def __str__(self) -> str:
        return f"filter[{self.field}][{self.operator}]={self.value}"

    def __hash__(self) -> int:
        return hash(str(self))

    @staticmethod
    def game_id() -> GamesFilter:
        return GamesFilter(field="game_id")

    @staticmethod
    def date_start() -> GamesFilter:
        return GamesFilter(field="date_start")

    @staticmethod
    def season() -> GamesFilter:
        return GamesFilter(field="season")

    @staticmethod
    def week() -> GamesFilter:
        return GamesFilter(field="week")

    @staticmethod
    def temperature() -> GamesFilter:
        return GamesFilter(field="temperature")

    @staticmethod
    def attendance() -> GamesFilter:
        return GamesFilter(field="attendance")

    @staticmethod
    def team() -> GamesFilter:
        return GamesFilter(field="team")

    @staticmethod
    def team_1() -> GamesFilter:
        return GamesFilter(field="team_1")

    @staticmethod
    def team_2() -> GamesFilter:
        return GamesFilter(field="team_2")

    @staticmethod
    def event_type_id() -> GamesFilter:
        return GamesFilter(field="event_type_id")

    def is_equal_to(self, value: int | str) -> GamesFilter:
        self.operator = "eq"
        self.value = value
        return self

    def is_not_equal_to(self, value: int | str) -> GamesFilter:
        self.operator = "ne"
        self.value = value
        return self

    def is_greater_than(self, value: int | str) -> GamesFilter:
        self.operator = "gt"
        self.value = value
        return self

    def is_less_than(self, value: int | str) -> GamesFilter:
        self.operator = "lt"
        self.value = value
        return self

    def is_greater_than_or_equal_to(self, value: int | str) -> GamesFilter:
        self.operator = "ge"
        self.value = value
        return self

    def is_less_than_or_equal_to(self, value: int | str) -> GamesFilter:
        self.operator = "le"
        self.value = value
        return self

    def is_in(self, value: int | str) -> GamesFilter:
        self.operator = "in"
        self.value = value
        return self


class GamesClient:
    def __init__(self, proxy: Proxy, season: Optional[int]):
        self.season = season
        self.proxy = proxy
        self.__filters: List[GamesFilter] = []

    def get(self, page_number: int = 1, page_size: int = 20) -> List[Game]:
        """
        Paging values are not applicable unless searching across seasons
        """
        path = "games"

        if self.season:
            path += f"/{self.season}"
        else:
            path += f"?page[number]={page_number}&page[size]={page_size}"

        filter_string = ""

        for filter in set(self.__filters):
            filter_string += f"&{str(filter)}"

        if "?" in path:
            path += filter_string
        else:
            path += f"?{filter_string[1:]}"  # strip the leading & and add ?

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"
        return [Game(**x) for x in data]

    def filter(self, filter: GamesFilter) -> GamesClient:
        self.__filters.append(filter)
        return self

    def game(self, game_id: int) -> GameClient:
        assert self.season, "Season must be provided to fetch individual games"
        return GameClient(self.proxy, self.season, game_id)
