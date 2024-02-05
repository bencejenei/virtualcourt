from virtualcourt.data.datafiles import team_bio_formatted, team_stats_formatted
import json


def main():
    pass


def load_teams_bio() -> dict:
    """Return dict of the team's bio located at:
        '.../virtualcourt/virtualcourt/data/formatted/team_bio_form.json'

    :return: teams_bio: dict
    """

    with open(team_bio_formatted(), "r") as bio:
        teams_bio: dict = json.load(bio)
    return teams_bio


def load_teams_stats() -> dict:
    """Return dict of the team's stats located at:
        '.../virtualcourt/virtualcourt/data/formatted/team_stats_form.json'

    :return: teams_stats: dict
    """

    with open(team_stats_formatted(), "r") as bio:
        teams_stat: dict = json.load(bio)
    return teams_stat


def extract_team_ids() -> list[int]:
    """Return a list with the team_id number of all teams

    :return: team_list: list[int]
    """

    teams_bio: dict = load_teams_bio()
    team_ids: list = []

    for team_bio in teams_bio:
        team_ids.append(team_bio)
    return team_ids


def extract_team_tags():
    """Return a list with the team_id number of all teams

    :return: team_tags: list[str]
    """

    teams_bio: dict = load_teams_bio()
    team_tags: list = []

    for team_bio in teams_bio:
        for values in team_bio.values():
            team_tags.append(values["team_tag"])
    return team_tags


def match_tag_to_id(id_to_find: int|str):
    """Return a dict object with team_id: team_tag key-value pair

    :param id_to_find: str | int
    :return: tag: dict{int: str}
    """
    if type(id_to_find) == str:
        id_to_find = int(id_to_find)
    teams_bio: dict = load_teams_bio()
    tag: dict = {}
    for team_bio in teams_bio.items():
        if id_to_find == int(team_bio[0]):
            tag = {id_to_find: team_bio[1]["team_tag"]}
            return tag
    return tag


if __name__ == "__main__":
    main()
