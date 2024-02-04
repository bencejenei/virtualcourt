import json

import team_helper
from virtualcourt.data.datafiles import team_bio_formatted, team_stats_formatted


def main():
    pass


class Team:
    teams_bio = json.load(open(team_bio_formatted(), "r"))

    def __init__(self, team_id, team_tag):
        self.team_id = team_id
        self.team_tag = team_tag

    @property
    def team_data(self):
        every_bio = json.load(open(team_bio_formatted(), "r"))
        print(every_bio[0])


def create_team_list():
    teams = {}

    for team_id in team_helper.extract_team_ids():
        teams.update({team_id: {"team_id": team_id,
                                "team_tag": team_helper.match_tag_to_id(team_id),
                                "team_class": Team(team_id, team_helper.match_tag_to_id(team_id))}})

    return teams


teams = create_team_list()

print(teams["1610612754"]["team_class"].team_data)

if __name__ == "__main__":
    create_team_list()
