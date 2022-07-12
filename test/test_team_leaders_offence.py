import os

import pytest

from cflpy.cfl_py import CflPy

CflPy.setup(os.environ.get("CFL_API_KEY"))

test_years = [
    (2019),
    (2021),
]


@pytest.mark.parametrize("season", test_years)
def test_game_stats(season):
    results = CflPy.v1_1().team_leaders(season).offence().get_game_stats()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_passing(season):
    results = CflPy.v1_1().team_leaders(season).offence().get_passing()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_rushing(season):
    results = CflPy.v1_1().team_leaders(season).offence().get_rushing()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_receiving(season):
    results = CflPy.v1_1().team_leaders(season).offence().get_receiving()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_kicking(season):
    results = CflPy.v1_1().team_leaders(season).offence().get_kicking()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_field_goals_converts(season):
    results = CflPy.v1_1().team_leaders(season).offence().get_field_goals_converts()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_punting_kickoffs(season):
    results = CflPy.v1_1().team_leaders(season).offence().get_punting_kickoffs()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_punt_kickoff_returns(season):
    results = CflPy.v1_1().team_leaders(season).offence().get_punt_kickoff_returns()
    assert isinstance(results, list)
