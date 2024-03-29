import json
from virtualcourt.data.datafiles import team_bio_raw, team_bio_formatted


def main():
    format_team_bio_file()


def format_team_bio_file() -> dict:
    """Convert and format 'team_stats.csv' to 'team_stats_form.json' and save it to
    '.../virtualcourt/virtualcourt/data/formatted/team_bio_form.json'

    input: JSON file, containing every team's bio
            location:   '.../virtualcourt/virtualcourt/data/raw/team_bio.json'
            file format: JSON

    output: JSON file, containing dict-style formatted team bio
            location: '.../virtualcourt/virtualcourt/data/formatted/team_bio_form.json'
            file format: JSON

    :return: team_database: dic
    """

    with open(team_bio_raw(), "r") as file:
        raw_file: list[list[str]] = json.load(file)
    team_database: dict = {}

    for entry in raw_file:
        temp_dict: dict = {entry[0]: {"team_id": entry[0],
                                      "team_tag": entry[1],
                                      "team_nickname": entry[2],
                                      "team_establishment": entry[3],
                                      "team_city": entry[4],
                                      "team_name": entry[5],
                                      "team_state": entry[6],
                                      "team_championship_years": entry[7]}
        }
        team_database.update(temp_dict)

    with open(team_bio_formatted(), "w") as file:
        file.write(json.dumps(team_database, indent=4))

    return team_database


if __name__ == "__main__":
    main()
