from __future__ import annotations

from pydantic import BaseModel


class Passing(BaseModel):
    season: int
    games_played: int
    points: int
    points_pgp: str
    attempts: int
    completions: int
    completion_pct: str
    attempts_pgp: str
    yards: int
    yards_average: str
    yards_pgp: str
    touchdowns: int
    interceptions: int
    first_downs_passing: int
    first_downs_pct: str
    long: int
    sacks: int
    team_abbreviation: str
    team_location: str
    team_nickname: str


class Rushing(BaseModel):
    season: int
    games_played: int
    points: int
    points_pgp: str
    attempts: int
    attempts_pgp: str
    yards: int
    yards_average: str
    yards_pgp: str
    touchdowns: int
    long: int
    first_downs_rushing: int
    first_downs_pct: str
    rush_min_10: int
    rush_min_20: int
    team_abbreviation: str
    team_location: str
    team_nickname: str


class Receiving(BaseModel):
    season: int
    games_played: int
    points: int
    points_pgp: str
    receptions: int
    yards: int
    yards_after_catch: int
    yards_average: str
    yards_pgp: str
    long: int
    touchdowns: int
    receive_min_30: int
    first_downs_receiving: int
    first_downs_pct: str
    fumbles: int
    team_abbreviation: str
    team_location: str
    team_nickname: str


class Tackles(BaseModel):
    season: int
    games_played: int
    tackles_total: int
    tackles_defensive: int
    tackles_specialteams: int
    tackles_for_loss: int
    sacks_qb_made: int
    interceptions_made: int
    interceptions_yards: int
    interceptions_long: int
    interceptions_touchdowns: int
    fumbles_forced: int
    fumble_returns: int
    fumble_returns_yards: int
    fumble_returns_long: int
    fumble_returns_touchdowns: int
    team_abbreviation: str
    team_location: str
    team_nickname: str
