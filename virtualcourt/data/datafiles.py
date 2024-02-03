import os
import virtualcourt.data.raw as rawfolder


def main():
    pass


def player_attributes():
    return f"{os.path.dirname(__file__)}/raw/player_attributes.json"


def player_stats():
    return f"{os.path.dirname(__file__)}/raw/player_stats.json"


if __name__ == "__main__":
    main()
