import os

import pytest

from cflpy.client import CflPy

CflPy.setup(os.environ.get("CFL_API_KEY"))

test_players = [
    (148680),
    (148636),
    (87742),
    (161788),
    (61988),
    (162585),
    (158665),
    (5962),  # QB
    (162746),  # WR
    (125917),  # RB
    (7611),  # DB
    (158244),  # K
]


@pytest.mark.parametrize(
    "page_number",
    [
        (1),
        (14),
        (25),
        (50),
        (100),
        (400),
    ],
)
def test_get_multiple(page_number):
    players = CflPy.players().get(page_number=page_number)
    assert players


@pytest.mark.parametrize("cfl_central_id", test_players)
def test_get_player(cfl_central_id):
    player = CflPy.players().player(cfl_central_id).get()
    assert player


@pytest.mark.parametrize("cfl_central_id", test_players)
def test_can_get_seasons(cfl_central_id):
    player = CflPy.players().player(cfl_central_id).with_seasons().get()
    assert player and player.seasons


@pytest.mark.parametrize("cfl_central_id", test_players)
def test_can_get_game_by_game(cfl_central_id):
    player = CflPy.players().player(cfl_central_id).with_game_by_game().get()
    assert player and player.game_by_game


def test_can_get_current_team():
    """This test will require updating periodically, as it requires an up to date player."""
    cfl_central_id = 162746  # Bralon Addison
    player = CflPy.players().player(cfl_central_id).with_current_team().get()
    assert player and player.team and player.team.is_set
