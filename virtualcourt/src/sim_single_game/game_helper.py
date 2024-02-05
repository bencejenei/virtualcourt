import virtualcourt.src.team.team_runner as team_runner
from typing import Type
from numpy.random import normal as normdistr


def import_team_cards(home_team_id: str, away_team_id: str):
    home_team_card: dict = {}
    away_team_card: dict = {}

    for key, value in team_runner.initial_team_class().items():
        if home_team_id == key:
            home_team_card = value
        if away_team_id == key:
            away_team_card = value
    return [home_team_card, away_team_card]


def extract_team_class(team_card):
    return team_card.get("team_class")


def get_pts_stat(team_class: Type[team_runner.Team]):
    all_team_stats: dict = team_class.team_stats
    points: int = int(normdistr(loc=float(all_team_stats.get("PTS")), scale=10))
    return points


def print_final_result(home_point, home_team, away_point, away_team):
    if home_point > away_point:
        winning_team = home_team
    elif home_point < away_point:
        winning_team = away_team
    else:
        print_final_result(home_point, home_team, away_point, away_team)
    print("The game is over. Final results:",
          f"{home_point} - {home_team}",
          f"{away_point} - {away_team}",
          f"{winning_team} won!", sep="\n")
