import json
import typing
from typing import Type

import virtualcourt.src.team.team_helper as team_helper
from virtualcourt.data.datafiles import team_bio_formatted, team_stats_formatted


def main():
    pass


class Team:
    with open(team_bio_formatted(), "r") as file:
        teams_bio: dict = json.load(file)
    with open(team_stats_formatted(), "r") as file:
        teams_stat: dict = json.load(file)

    def __init__(self, team_id: str, team_tag: str):
        self.bio: dict = Team.teams_bio[str(team_id)]
        self.stats: dict = Team.teams_stat[str(team_id)]
        self.team_id: str = str(team_id)
        self.team_tag: str = team_tag
        self.team_nickname: str = self.bio["team_nickname"]
        self.team_establishment: int = self.bio["team_establishment"]
        self.team_city: str = self.bio["team_city"]
        self.team_name: str = self.bio["team_name"]
        self.team_state: str = self.bio["team_state"]
        self.team_championship_years: list[int] = self.bio["team_championship_years"]

    def __str__(self):
        return str({"bio": self.bio, "stats": self.stats})


def create_team_list() -> dict:
    team_dict: dict = {}
    for team_id in team_helper.extract_team_ids():
        team_card: dict = {team_id: {"team_id": int(team_id),
                                     "team_tag": list(team_helper.match_tag_to_id(team_id).values())[0],
                                     "team_class": Team(team_id=str(team_id),
                                                        team_tag=list(team_helper.match_tag_to_id(team_id).values())[0])}}
        team_dict.update(team_card)
    return team_dict


def extract_data(team_id: str, list_of_teams) -> typing.Any:
    team_one: Type[Team] = list_of_teams[team_id]["team_class"]
    print(team_one.__dict__)


def initial_team_class() -> dict:
    return create_team_list()


if __name__ == "__main__":
    main()
