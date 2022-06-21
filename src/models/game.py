# generated by datamodel-codegen:
#   filename:  game.json
#   timestamp: 2022-06-20T20:51:52+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class EventType(BaseModel):
    event_type_id: int
    name: str
    title: str


class EventStatus(BaseModel):
    event_status_id: int
    name: str
    is_active: bool
    quarter: Optional[int]
    minutes: Optional[int]
    seconds: Optional[int]
    down: Optional[int]
    yards_to_go: Optional[int]


class Venue(BaseModel):
    venue_id: int
    name: str


class Weather(BaseModel):
    temperature: int
    sky: str
    wind_speed: str
    wind_direction: str
    field_conditions: str


class CoinToss(BaseModel):
    coin_toss_winner: str
    coin_toss_winner_election: str


class Linescore(BaseModel):
    quarter: int | str
    score: int


class Team(BaseModel):
    team_id: int
    location: str
    nickname: str
    abbreviation: str
    score: int
    venue_id: int
    linescores: List[Linescore]
    is_at_home: bool
    is_winner: Optional[bool]


class Down(BaseModel):
    down: int
    attempts: int
    yards: int


class Offence(BaseModel):
    offence_possession_time: str
    downs: List[Down]


class Turnovers(BaseModel):
    fumbles: int
    interceptions: int
    downs: int


class Passing(BaseModel):
    pass_attempts: int
    pass_completions: int
    pass_net_yards: int
    pass_long: int
    pass_touchdowns: int
    pass_completion_percentage: str
    pass_efficiency: str
    pass_interceptions: int
    pass_fumbles: int


class Rushing(BaseModel):
    rush_attempts: int
    rush_net_yards: int
    rush_long: int
    rush_touchdowns: int
    rush_long_touchdowns: int


class Receiving(BaseModel):
    receive_attempts: int
    receive_caught: int
    receive_yards: int
    receive_long: int
    receive_touchdowns: int
    receive_long_touchdowns: int
    receive_yards_after_catch: int
    receive_fumbles: int


class Punts(BaseModel):
    punts: int
    punt_yards: int
    punt_net_yards: int
    punt_long: int
    punt_singles: int
    punts_blocked: int
    punts_in_10: int
    punts_in_20: int
    punts_returned: int


class PuntReturns(BaseModel):
    punt_returns: int
    punt_returns_yards: int
    punt_returns_touchdowns: int
    punt_returns_long: int
    punt_returns_touchdowns_long: int


class KickReturns(BaseModel):
    kick_returns: int
    kick_returns_yards: int
    kick_returns_touchdowns: int
    kick_returns_long: int
    kick_returns_touchdowns_long: int


class FieldGoals(BaseModel):
    field_goal_attempts: int
    field_goal_made: int
    field_goal_yards: int
    field_goal_singles: int
    field_goal_long: int
    field_goal_points: int


class Kicking(BaseModel):
    kicks: int
    kick_yards: int
    kicks_net_yards: int
    kicks_long: int
    kicks_singles: int
    kicks_out_of_end_zone: int
    kicks_onside: int


class OnePointConverts(BaseModel):
    attempts: int
    made: int


class TwoPointConverts(BaseModel):
    attempts: int
    made: int


class Converts(BaseModel):
    one_point_converts: OnePointConverts
    two_point_converts: TwoPointConverts


class Defence(BaseModel):
    tackles_total: int
    tackles_defensive: int
    tackles_special_teams: int
    sacks_qb_made: int
    interceptions: int
    fumbles_forced: int
    fumbles_recovered: int
    passes_knocked_down: int
    defensive_touchdowns: int
    defensive_safeties: int


class Penalties(BaseModel):
    total: int
    yards: int
    offence_total: int
    offence_yards: int
    defence_total: int
    defence_yards: int
    special_teams_coverage_total: int
    special_teams_coverage_yards: int
    special_teams_return_total: int
    special_teams_return_yards: int


class Player(BaseModel):
    cfl_central_id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: str


class PassingItem(BaseModel):
    player: Player
    pass_attempts: int
    pass_completions: int
    pass_net_yards: int
    pass_long: int
    pass_touchdowns: int
    pass_completion_percentage: str
    pass_efficiency: str
    pass_interceptions: int
    pass_fumbles: int


class RushingItem(BaseModel):
    player: Player
    rush_attempts: int
    rush_net_yards: int
    rush_long: int
    rush_touchdowns: int
    rush_long_touchdowns: int


class ReceivingItem(BaseModel):
    player: Player
    receive_attempts: int
    receive_caught: int
    receive_yards: int
    receive_long: int
    receive_touchdowns: int
    receive_long_touchdowns: int
    receive_yards_after_catch: int
    receive_fumbles: int


class Punt(BaseModel):
    player: Player
    punts: int
    punt_yards: int
    punt_net_yards: int
    punt_long: int
    punt_singles: int
    punts_blocked: int
    punts_in_10: int
    punts_in_20: int
    punts_returned: int


class PuntReturn(BaseModel):
    player: Player
    punt_returns: int
    punt_returns_yards: int
    punt_returns_touchdowns: int
    punt_returns_long: int
    punt_returns_touchdowns_long: int


class KickReturn(BaseModel):
    player: Player
    kick_returns: int
    kick_returns_yards: int
    kick_returns_touchdowns: int
    kick_returns_long: int
    kick_returns_touchdowns_long: int


class FieldGoal(BaseModel):
    player: Player
    field_goal_attempts: int
    field_goal_made: int
    field_goal_yards: int
    field_goal_singles: int
    field_goal_long: int
    field_goal_missed_list: str
    field_goal_points: int


class KickingItem(BaseModel):
    player: Player
    kicks: int
    kick_yards: int
    kicks_net_yards: int
    kicks_long: int
    kicks_singles: int
    kicks_out_of_end_zone: int
    kicks_onside: int


class OnePointConvert(BaseModel):
    player: Player
    one_point_converts_attempts: int
    one_point_converts_made: int


class DefenceItem(BaseModel):
    player: Player
    tackles_total: int
    tackles_defensive: int
    tackles_special_teams: int
    sacks_qb_made: int
    interceptions: int
    fumbles_forced: int
    fumbles_recovered: int
    passes_knocked_down: int


class Players(BaseModel):
    passing: List[PassingItem]
    rushing: List[RushingItem]
    receiving: List[ReceivingItem]
    punts: List[Punt]
    punt_returns: List[PuntReturn]
    kick_returns: List[KickReturn]
    field_goals: List[FieldGoal]
    field_goal_returns: List
    kicking: List[KickingItem]
    one_point_converts: List[OnePointConvert]
    two_point_converts: List
    defence: List[DefenceItem]


class BoxscoreTeam(BaseModel):
    abbreviation: str
    team_id: int
    offence: Optional[Offence]
    turnovers: Optional[Turnovers]
    passing: Optional[Passing]
    rushing: Optional[Rushing]
    receiving: Optional[Receiving]
    punts: Optional[Punts]
    punt_returns: Optional[PuntReturns]
    kick_returns: Optional[KickReturns]
    field_goals: Optional[FieldGoals]
    kicking: Optional[Kicking]
    converts: Optional[Converts]
    defence: Optional[Defence]
    penalties: Optional[Penalties]
    players: Players


class BoxscoreTeams(BaseModel):
    team_1: BoxscoreTeam
    team_2: BoxscoreTeam


class Boxscore(BaseModel):
    teams: BoxscoreTeams


class Quarterback(BaseModel):
    cfl_central_id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: str


class BallCarrier(BaseModel):
    cfl_central_id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: str


class PrimaryDefender(BaseModel):
    cfl_central_id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: str


class PlayersInPlay(BaseModel):
    quarterback: Player
    ball_carrier: Player
    primary_defender: Player


class PlayByPlayItem(BaseModel):
    play_id: int
    play_sequence: int
    quarter: int
    play_clock_start: str
    play_clock_start_in_secs: int
    field_position_start: str
    field_position_end: str
    down: int
    yards_to_go: int
    is_in_red_zone: bool
    team_home_score: int
    team_visitor_score: int
    play_type_id: int
    play_type_description: str
    play_result_type_id: int
    play_result_type_description: str
    play_result_yards: int
    play_result_points: int
    play_success_id: int
    play_success_description: str
    play_change_of_possession_occurred: bool
    team_abbreviation: str
    team_id: int
    players: PlayersInPlay
    play_summary: str


class RosterItem(BaseModel):
    cfl_central_id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: str
    uniform: int
    position: str
    is_national: bool
    is_starter: bool
    is_inactive: bool


class RosterTeam(BaseModel):
    abbreviation: str
    team_id: int
    roster: List[RosterItem]


class RosterItem1(BaseModel):
    cfl_central_id: int
    first_name: str
    middle_name: str
    last_name: str
    birth_date: str
    uniform: int
    position: str
    is_national: bool
    is_starter: bool
    is_inactive: bool


class Team22(BaseModel):
    abbreviation: str
    team_id: int
    roster: List[RosterItem1]


class RosterTeams(BaseModel):
    team_1: RosterTeam
    team_2: RosterTeam


class Rosters(BaseModel):
    teams: RosterTeams


class Penalty(BaseModel):
    play_id: int
    play_sequence: int
    quarter: int
    play_clock_start: str
    play_clock_start_in_secs: int
    play_summary: str
    field_position_start: str
    field_position_end: str
    down: int
    yards_to_go: int
    penalty_id: int
    penalty_code: str
    penalty_name: str
    penalty_type_id: int
    penalty_type_name: str
    penalty_situation_id: int
    penalty_situation_code: str
    penalty_situation_name: str
    is_major: int
    was_accepted: int
    team_or_player_penalty: str
    team_abbreviation: str
    team_id: int
    game_id: int
    cfl_central_id: int
    first_name: str
    middle_name: str
    last_name: str


class PlayReview(BaseModel):
    play_id: int
    quarter: int
    play_clock_start: str
    play_clock_start_in_secs: int
    play_summary: str
    field_position_start: str
    field_position_end: str
    down: int
    yards_to_go: int
    play_type_id: int
    play_type_description: str
    play_review_type_id: int
    play_review_type_name: str
    play_reversed_on_review: bool
    game_id: int


class Game(BaseModel):
    game_id: int
    date_start: str
    game_number: int
    week: int
    season: int
    attendance: int
    game_duration: Optional[int]
    event_type: EventType
    event_status: EventStatus
    venue: Venue
    weather: Weather
    coin_toss: CoinToss
    tickets_url: str
    team_1: Team
    team_2: Team
    boxscore: Optional[Boxscore]
    play_by_play: Optional[List[PlayByPlayItem]]
    rosters: Optional[Rosters]
    penalties: Optional[List[Penalty]]
    play_reviews: Optional[List[PlayReview]]
