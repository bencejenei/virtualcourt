import json
from virtualcourt.data.datafiles import team_bio_raw, team_bio_formatted


def main():
    format_team_bio_file()


def format_team_bio_file() -> None:
    """Overwrite '.../data/formatted/team_bio_form' file.
    input: team bio file located at '.../data/raw/team_bio_form'
    output: datafile, containing dict-style formatted team bio
    """

    raw_file: list[list[str]] = json.load(open(team_bio_raw(), "r"))
    team_database: list = []

    for entry in raw_file:
        print(entry)
        temp_dict: dict = {"team_id": entry[0],
                     "team_tag": entry[1],
                     "team_nickname": entry[2],
                     "team_establishment": entry[3],
                     "team_city": entry[4],
                     "team_name": entry[5],
                     "team_state": entry[6],
                     "team_championship_years": entry[7]
        }
        team_database.append(temp_dict)

    open(team_bio_formatted(), "w").write(json.dumps(team_database, indent=4))


if __name__ == "__main__":
    main()