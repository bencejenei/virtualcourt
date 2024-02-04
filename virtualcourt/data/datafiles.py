import os
import virtualcourt.data.raw as rawfolder


def main():
    pass


def player_attributes_raw() -> str:
    """Returns string of path of "player_attributes.json" file in "...data/raw" Folder.
    :argument: None

    :return: string of path of "player_attributes.json" file in "...data/raw" Folder.
    :rtype: str
    """
    return f"{os.path.dirname(__file__)}/raw/player_attributes.json"


def player_stats_raw():
    return f"{os.path.dirname(__file__)}/raw/player_stats.json"


def team_stats_raw():
    return f"{os.path.dirname(__file__)}/raw/team_stats.csv"


def team_stats_formatted():
    return f"{os.path.dirname(__file__)}/formatted/team_stats_form.json"


if __name__ == "__main__":
    main()
