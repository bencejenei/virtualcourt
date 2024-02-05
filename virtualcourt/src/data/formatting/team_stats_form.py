import csv
import json
from virtualcourt.data.datafiles import team_stats_raw, team_bio_formatted, team_stats_formatted


def main():
    format_team_stats_file()
    pass


def format_team_stats_file() -> dict:
    """Convert and format 'team_stats.csv' to 'team_stats_form.json' and save it to
    '.../virtualcourt/virtualcourt/data/formatted/team_stats_form.json'

    input: CSV file, containing every team's selected stats
            location:   '.../virtualcourt/virtualcourt/data/raw/tems_stats.csv'
            file format: CSV

    output: JSON file, containing dict-style formatted team bio
            location: '.../virtualcourt/virtualcourt/data/formatted/teams_stats_form.json'
            file format: JSON

    :return: team_stats: dict
    """

    with open(team_bio_formatted(), mode='r') as file:
        team_bio = json.load(file)

    with open(team_stats_raw(), mode='r', encoding='utf-8-sig') as file:
        raw_team_stats = file
        csv_file: csv.DictReader[str] = csv.DictReader(raw_team_stats, quotechar=",")
        team_stats: dict = {}
        for row in csv_file:
            for team in team_bio.values():
                for value in team:
                    if value == "team_name":
                        if team["team_name"] == row["Team"]:
                            team_stats.update({team["team_id"]: row})

    with open(team_stats_formatted(), "w") as file:
        file.write(json.dumps(team_stats, indent=4))

    return team_stats


if __name__ == "__main__":
    main()

format_team_stats_file()