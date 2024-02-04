import csv
import json
from virtualcourt.data.datafiles import team_stats_raw, team_bio_formatted, team_stats_formatted


def main():
    format_team_stats_file()
    pass


def format_team_stats_file() -> None:
    raw_team_stats = open(team_stats_raw(), mode='r', encoding='utf-8-sig')
    team_bio = json.load(open(team_bio_formatted(), mode='r'))

    csv_file = csv.DictReader(raw_team_stats, quotechar=",")
    team_stats: list = []

    for row in csv_file:
        print(row)
        for team in team_bio:
            if (team["team_name"]) == row["Team"]:
                print(team["team_id"])
                row.update({"team_id": team["team_id"]})
        team_stats.append(row)

    open(team_stats_formatted(), "w").write(json.dumps(team_stats, indent=4))


if __name__ == "__main__":
    main()
