import os

import pytest

from cflpy.client import CflPy

CflPy.setup(os.environ.get("CFL_API_KEY"))

test_seasons = [
    (2018),
    (2021),
]


@pytest.mark.parametrize("season", test_seasons)
def test_can_get_standings(season):
    standings = CflPy.standings(season).get()
    assert standings and standings.divisions
