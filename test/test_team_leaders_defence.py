import os

import pytest

from cflpy.cfl_py import CflPy

CflPy.setup(os.environ.get("CFL_API_KEY"))

test_years = [
    (2019),
    (2021),
]


@pytest.mark.parametrize("season", test_years)
def test_passing(season):
    results = CflPy.v1_1().team_leaders(season).defence().get_passing()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_rushing(season):
    results = CflPy.v1_1().team_leaders(season).defence().get_rushing()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_receiving(season):
    results = CflPy.v1_1().team_leaders(season).defence().get_receiving()
    assert isinstance(results, list)


@pytest.mark.parametrize("season", test_years)
def test_tackles(season):
    results = CflPy.v1_1().team_leaders(season).defence().get_tackles()
    assert isinstance(results, list)
