import csv
import json
from virtualcourt.data import datafiles


def main():
    format_team_stats_file()
    pass


def format_team_stats_file():
    raw_file = datafiles.team_stats_raw()

    with open(raw_file, mode='r', encoding='utf-8-sig')as file:
        csv_file = csv.DictReader(file, quotechar=",")

        for row in csv_file:
            print(json.dumps(row, indent=4))


if __name__ == "__main__":
    main()
