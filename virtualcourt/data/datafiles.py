import os
import virtualcourt.data.raw as rawfolder


def main():
    print(player_attributes())


def player_attributes():
    return f"{os.path.dirname(__file__)}/raw/player_attributes.json"


if __name__ == "__main__":
    main()
