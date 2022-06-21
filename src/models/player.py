# generated by datamodel-codegen:
#   filename:  player.json
#   timestamp: 2022-06-21T14:54:41+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class School(BaseModel):
    school_id: int
    name: str


class Position(BaseModel):
    position_id: int
    offence_defence_or_special: str
    abbreviation: str
    description: str


class Team(BaseModel):
    is_set: bool
    team_id: Optional[int]
    location: Optional[str]
    nickname: Optional[str]
    abbreviation: Optional[str]
    season: Optional[int]
    uniform: Optional[int]


class SeasonDefence(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    tackles_total: int
    tackles_yards: int
    tackles_defensive: int
    tackles_specialteams: int
    tackles_for_loss: int
    sacks_qb_made: int
    interceptions_made: int
    interceptions_yards: int
    interceptions_long: int
    interceptions_touchdowns: int
    interceptions_touchdowns_long: int
    fumbles_forced: int
    fumble_returns: int
    fumble_returns_yards: int
    fumble_returns_long: int
    fumble_returns_touchdowns: int
    fumble_returns_touchdowns_long: int
    passes_knocked_down: int


class SeasonFieldGoals(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    field_goals_attempts: int
    field_goals_made: int
    field_goals_long: int
    field_goals_singles: int
    field_goals_blocked: int
    field_goals_made_01_19: int
    field_goals_made_20_29: int
    field_goals_made_30_39: int
    field_goals_made_40_49: int
    field_goals_made_50_plus: int
    extra_point_attempts: int
    extra_point_made: int
    extra_point_yards: int
    points: int


class SeasonPunts(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    punts: int
    punts_yards: int
    punts_net_yards: int
    punts_long: int
    punts_singles: int
    punts_blocked: int
    punts_in_10: int
    punts_in_20: int
    punts_returned: int


class SeasonKickoffs(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    kickoffs: int
    kickoffs_yards: int
    kickoffs_net_yards: int
    kickoffs_long: int
    kickoffs_singles: int
    kickoffs_onside: int


class SeasonPassing(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    pass_attempts: int
    pass_completions: int
    pass_percentage: str
    pass_net_yards: int
    pass_long: int
    pass_touchdowns: int
    pass_touchdowns_long: int
    pass_interceptions: int
    pass_fumbles: int
    pass_efficiency: str
    pass_interceptions_percentage: str


class SeasonRushing(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    rush_attempts: int
    rush_yards: int
    rush_average: str
    rush_long: int
    rush_touchdowns: int
    rush_touchdowns_long: int
    rush_min_10: int
    rush_min_20: int


class SeasonPuntReturns(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    punt_returns: int
    yards: int
    average: str
    long: int
    touchdowns: int
    touchdowns_long: int


class SeasonKickoffReturns(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    kickoff_returns: int
    yards: int
    average: str
    long: int
    touchdowns: int
    touchdowns_long: int


class SeasonMissedFgReturn(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    missed_fg_returns: int
    yards: int
    average: str
    long: int
    touchdowns: int
    touchdowns_long: int


class SeasonReceiving(BaseModel):
    season: int
    team_abbreviation: str
    games_played: int
    receive_attempts: int
    receive_caught: int
    receive_average: str
    receive_yards: int
    receive_long: int
    receive_touchdowns: int
    receive_touchdowns_long: int
    receive_second_down_conversions: int
    receive_fumbles: int
    receive_yards_after_catch: int
    receive_min_30: int


class Seasons(BaseModel):
    defence: Optional[List[SeasonDefence]]
    field_goals: Optional[List[SeasonFieldGoals]]
    punts: Optional[List[SeasonPunts]]
    kickoffs: Optional[List[SeasonKickoffs]]
    passing: Optional[List[SeasonPassing]]
    rushing: Optional[List[SeasonRushing]]
    punt_returns: Optional[List[SeasonPuntReturns]]
    kickoff_returns: Optional[List[SeasonKickoffReturns]]
    missed_fg_returns: Optional[List[SeasonMissedFgReturn]]
    receiving: Optional[List[SeasonReceiving]]


class GameDefence(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    tackles_total: int
    tackles_yards: int
    tackles_defensive: int
    tackles_specialteams: int
    tackles_for_loss: int
    sacks_qb_made: int
    interceptions_made: int
    interceptions_yards: int
    interceptions_long: int
    interceptions_touchdowns: int
    interceptions_touchdowns_long: int
    fumbles_forced: int
    fumble_returns: int
    fumble_returns_yards: int
    fumble_returns_long: int
    fumble_returns_touchdowns: int
    fumble_returns_touchdowns_long: int
    passes_knocked_down: int


class GameFieldGoals(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    field_goals_attempts: int
    field_goals_made: int
    field_goals_long: int
    field_goals_singles: int
    field_goals_blocked: int
    field_goals_made_01_19: int
    field_goals_made_20_29: int
    field_goals_made_30_39: int
    field_goals_made_40_49: int
    field_goals_made_50_plus: int
    extra_point_attempts: int
    extra_point_made: int
    extra_point_yards: int
    points: int


class GamePunts(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    punts: int
    punts_yards: int
    punts_net_yards: int
    punts_long: int
    punts_singles: int
    punts_blocked: int
    punts_in_10: int
    punts_in_20: int
    punts_returned: int


class GameKickoffs(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    kickoffs: int
    kickoffs_yards: int
    kickoffs_net_yards: int
    kickoffs_long: int
    kickoffs_singles: int
    kickoffs_onside: int


class GamePassing(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    pass_attempts: int
    pass_completions: int
    pass_percentage: str
    pass_net_yards: int
    pass_long: int
    pass_touchdowns: int
    pass_touchdowns_long: int
    pass_interceptions: int
    pass_fumbles: int
    pass_efficiency: str
    pass_interceptions_percentage: str


class GameRushing(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    rush_attempts: int
    rush_yards: int
    rush_average: str
    rush_long: int
    rush_touchdowns: int
    rush_touchdowns_long: int
    rush_min_10: int
    rush_min_20: int


class GamePuntReturns(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    punt_returns: int
    yards: int
    average: str
    long: int
    touchdowns: int
    touchdowns_long: int


class GameKickoffReturns(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    kickoff_returns: int
    yards: int
    average: str
    long: int
    touchdowns: int
    touchdowns_long: int


class GameMissFgReturns(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    missed_fg_returns: int
    yards: int
    average: str
    long: int
    touchdowns: int
    touchdowns_long: int


class GameReceiving(BaseModel):
    game_id: int
    game_date: str
    week: int
    season: int
    opponent_team_abbreviation: str
    receive_attempts: int
    receive_caught: int
    receive_average: str
    receive_yards: int
    receive_long: int
    receive_touchdowns: int
    receive_touchdowns_long: int
    receive_second_down_conversions: int
    receive_fumbles: int
    receive_yards_after_catch: int
    receive_min_30: int


class GameByGame(BaseModel):
    defence: Optional[List[GameDefence]]
    field_goals: Optional[List[GameFieldGoals]]
    punts: Optional[List[GamePunts]]
    kickoffs: Optional[List[GameKickoffs]]
    passing: Optional[List[GamePassing]]
    rushing: Optional[List[GameRushing]]
    punt_returns: Optional[List[GamePuntReturns]]
    kickoff_returns: Optional[List[GameKickoffReturns]]
    missed_fg_returns: Optional[List[GameMissFgReturns]]
    receiving: Optional[List[GameReceiving]]


class Player(BaseModel):
    cfl_central_id: int
    stats_inc_id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: str
    birth_place: str
    height: Optional[str]
    weight: int
    rookie_year: Optional[int]
    foreign_player: bool
    image_url: Optional[str]
    school: School
    position: Position
    team: Optional[Team]
    seasons: Optional[Seasons]
    game_by_game: Optional[GameByGame]
