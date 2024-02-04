import team_helper


def main():
    pass


class Team:
    def __init__(self, team_id, team_tag):
        self.team_id = team_id
        self.team_tag = team_tag


def create_team_list():
    teams = {}

    for team_id in team_helper.extract_team_ids():
        teams.update({team_id: {"team_id": team_id,
                                "team_tag": team_helper.match_tag_to_id(team_id),
                                "team_class": Team(team_id, team_helper.match_tag_to_id(team_id))}})

    return teams


teams = create_team_list()

print(teams["1610612754"]["team_class"].team_tag)

if __name__ == "__main__":
    create_team_list()
