from cflpy.models.game import Team


def test_team_is_hashable():
    team = Team(
        team_id=1,
        location="Test",
        nickname="Team",
        abbreviation="TM",
        score=0,
        venue_id=0,
        is_at_home=True,
    )

    set([team])


def test_team_equality():
    team1 = Team(
        team_id=1,
        location="Test",
        nickname="Team",
        abbreviation="TM",
        score=0,
        venue_id=0,
        is_at_home=True,
    )

    team2 = team1.copy()

    assert team1 == team2
