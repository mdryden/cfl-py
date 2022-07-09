import os
from test.asserts import are_equal

import pytest

from cflpy.client import CflPy
from cflpy.clients.games import GamesFilter
from cflpy.models.game import Game

CflPy.setup(os.environ.get("CFL_API_KEY"))

test_games = [
    (2022, 6215),
    (2022, 6217),
    (2022, 6218),
    (2022, 6290),
    (2022, 6294),
]


def test_get_many_returns_list():
    games = CflPy.games(2022).get()
    assert isinstance(games, list)


def test_get_one_returns_list():
    game = CflPy.games(2022).game(6217).get()
    assert isinstance(game, Game)


@pytest.mark.parametrize("season,game_id", test_games)
def test_can_get_boxscore(season, game_id):
    game = CflPy.games(season).game(game_id).with_boxscore().get()
    assert game and game.boxscore


def test_can_get_play_by_play():
    game = CflPy.games(2022).game(6211).with_play_by_play().get()
    assert game and game.play_by_play


@pytest.mark.parametrize("season,game_id", test_games)
def test_can_get_rosters(season, game_id):
    game = CflPy.games(season).game(game_id).with_rosters().get()
    assert game and game.rosters


def test_can_get_penalties():
    game = CflPy.games(2022).game(6217).with_penalties().get()
    assert game and game.penalties


def test_can_get_play_reviews():
    game = CflPy.games(2022).game(6217).with_play_reviews().get()
    assert game and game.play_reviews


@pytest.mark.parametrize("season,game_id", test_games)
def test_can_get_all_data(season, game_id):
    game = CflPy.games(season).game(game_id).with_all().get()
    assert game


@pytest.mark.parametrize(
    "page_number,page_size,expected_first_game",
    [
        (1, 20, 2837),
        (2, 10, 2847),
    ],
)
def test_can_page_results(page_number, page_size, expected_first_game):
    games = CflPy.games().get(page_number=page_number, page_size=page_size)
    assert games and games[0].game_id == expected_first_game


# TODO: more test cases
@pytest.mark.parametrize(
    "filter,expected_first_game",
    [
        (GamesFilter.game_id().is_equal_to(5524), 5524),
        (GamesFilter.game_id().is_less_than(5524), 2837),
        (GamesFilter.event_type_id().is_not_equal_to(4), 2850),
    ],
)
def test_filter_results(filter: GamesFilter, expected_first_game):
    games = CflPy.games().filter(filter).get()
    assert games
    are_equal(expected_first_game, games[0].game_id)


def test_multiple_filters():
    games = (
        CflPy.games(2022)
        .filter(GamesFilter.event_type_id().is_not_equal_to(0))
        .filter(GamesFilter.team().is_equal_to("OTT"))
        .get()
    )

    assert games

    expected = 6212
    actual = games[0].game_id
    print(CflPy.proxy.last_url)

    are_equal(expected, actual)
