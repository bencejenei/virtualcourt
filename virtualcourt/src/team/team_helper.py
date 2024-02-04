from virtualcourt.data.datafiles import team_bio_formatted, team_stats_formatted
import json


def main():
    pass


def load_teams_bio():
    with open(team_bio_formatted(), "r") as bio:
        teams_bio = json.load(bio)
    return teams_bio


def load_teams_stats():
    with open(team_stats_formatted(), "r") as bio:
        teams_stat = json.load(bio)
    return teams_stat


def extract_team_ids():
    teams_bio = load_teams_bio()
    team_ids = []

    for team_bio in teams_bio:
        team_ids.append(team_bio)

    return team_ids


def extract_team_tags():
    teams_bio = load_teams_bio()
    team_tags = []

    for team_bio in teams_bio:
        for values in team_bio.values():
            team_tags.append(values["team_tag"])

    return team_tags


def match_tag_to_id(id_to_find):
    teams_bio = load_teams_bio()
    tag = ""
    for team_bio in teams_bio.items():
        x = team_bio[0]
        if id_to_find == team_bio[0]:
            tag = team_bio[1]["team_tag"]
        else:
            pass
    return tag


if __name__ == "__main__":
    main()
