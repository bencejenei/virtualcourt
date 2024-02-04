import csv
import json
from virtualcourt.data import datafiles


def main():
    format_team_stats_file()
    pass


def format_team_stats_file() -> None:
    raw_file = datafiles.team_stats_raw()

    with open(raw_file, mode='r', encoding='utf-8-sig')as file:
        csv_file = csv.DictReader(file, quotechar=",")

        team_stats = []
        for row in csv_file:
            team_stats.append(row)
        open(datafiles.team_stats_formatted(), "w").write(json.dumps(team_stats, indent=4))


if __name__ == "__main__":
    main()
