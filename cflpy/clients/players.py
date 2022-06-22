from __future__ import annotations

from datetime import date
from typing import List, Literal, Optional

from pydantic import BaseModel

from cflpy.models.player import Player
from cflpy.proxy import Proxy


class PlayerClient:
    def __init__(self, proxy: Proxy, cfl_central_id: int):
        assert cfl_central_id, "cfl_central_id must be provided"
        self.proxy = proxy
        self.cfl_central_id = cfl_central_id
        self.__includes: List[str] = []

    def get(self) -> Optional[Player]:
        path = f"players/{self.cfl_central_id}"

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
            return Player(**data[0])

    def with_seasons(self) -> PlayerClient:
        self.__includes.append("seasons")
        return self

    def with_game_by_game(self) -> PlayerClient:
        self.__includes.append("game_by_game")
        return self

    def with_current_team(self) -> PlayerClient:
        self.__includes.append("current_team")
        return self


class PlayersFilter(BaseModel):
    field: Literal[
        "cfl_central_id",
        "first_name",
        "middle_name",
        "name",
        "birth_date",
        "height",
        "weight",
        "rookie_year",
        "foreign_player",
        "school_id",
        "school_name",
        "position_id",
        "position_abbreviation",
        "offence_defence_or_special",
        "season",
        "game_id",
        "game_date",
    ]

    operator: Literal["eq", "ne", "gt", "lt", "ge", "le", "in", "like"] = "eq"

    value: str | int | date = ""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PlayersFilter):
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
    def cfl_central_id() -> PlayersFilter:
        return PlayersFilter(field="cfl_central_id")

    @staticmethod
    def first_name() -> PlayersFilter:
        return PlayersFilter(field="first_name")

    @staticmethod
    def middle_name() -> PlayersFilter:
        return PlayersFilter(field="middle_name")

    @staticmethod
    def last_name() -> PlayersFilter:
        return PlayersFilter(field="last_name")

    @staticmethod
    def name() -> PlayersFilter:
        return PlayersFilter(field="name")

    @staticmethod
    def birth_date() -> PlayersFilter:
        return PlayersFilter(field="birth_date")

    @staticmethod
    def height() -> PlayersFilter:
        return PlayersFilter(field="height")

    @staticmethod
    def weight() -> PlayersFilter:
        return PlayersFilter(field="weight")

    @staticmethod
    def rookie_year() -> PlayersFilter:
        return PlayersFilter(field="rookie_year")

    @staticmethod
    def foreign_player() -> PlayersFilter:
        return PlayersFilter(field="foreign_player")

    @staticmethod
    def school_id() -> PlayersFilter:
        return PlayersFilter(field="school_id")

    @staticmethod
    def school_name() -> PlayersFilter:
        return PlayersFilter(field="school_name")

    @staticmethod
    def position_id() -> PlayersFilter:
        return PlayersFilter(field="position_id")

    @staticmethod
    def position_abbreviation() -> PlayersFilter:
        return PlayersFilter(field="position_abbreviation")

    @staticmethod
    def offence_defence_or_special() -> PlayersFilter:
        return PlayersFilter(field="offence_defence_or_special")

    @staticmethod
    def season() -> PlayersFilter:
        return PlayersFilter(field="season")

    @staticmethod
    def game_id() -> PlayersFilter:
        return PlayersFilter(field="game_id")

    @staticmethod
    def game_date() -> PlayersFilter:
        return PlayersFilter(field="game_date")

    def is_equal_to(self, value: int | str) -> PlayersFilter:
        self.operator = "eq"
        self.value = value
        return self

    def is_not_equal_to(self, value: int | str) -> PlayersFilter:
        self.operator = "ne"
        self.value = value
        return self

    def is_greater_than(self, value: int | str) -> PlayersFilter:
        self.operator = "gt"
        self.value = value
        return self

    def is_less_than(self, value: int | str) -> PlayersFilter:
        self.operator = "lt"
        self.value = value
        return self

    def is_greater_than_or_equal_to(self, value: int | str) -> PlayersFilter:
        self.operator = "ge"
        self.value = value
        return self

    def is_less_than_or_equal_to(self, value: int | str) -> PlayersFilter:
        self.operator = "le"
        self.value = value
        return self

    def is_in(self, value: int | str) -> PlayersFilter:
        self.operator = "in"
        self.value = value
        return self

    def is_like(self, value: int | str) -> PlayersFilter:
        self.operator = "like"
        self.value = value
        return self


class PlayersClient:
    def __init__(self, proxy: Proxy):
        self.proxy = proxy
        self.__filters: List[PlayersFilter] = []

    def get(self, page_number: int = 1, page_size: int = 20) -> List[Player]:
        path = "players"

        path += f"?page[number]={page_number}&page[size]={page_size}"

        filter_string = ""

        for filter in set(self.__filters):
            filter_string += f"&{str(filter)}"

        path += filter_string

        data = self.proxy.get(path)
        assert isinstance(data, list), "Unexpected result from CFL API"
        return [Player(**x) for x in data]

    def filter(self, filter: PlayersFilter) -> PlayersClient:
        self.__filters.append(filter)
        return self

    def player(self, cfl_central_id: int) -> PlayerClient:
        return PlayerClient(self.proxy, cfl_central_id)
