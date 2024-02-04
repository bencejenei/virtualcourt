from bs4 import BeautifulSoup
import requests
import json
from virtualcourt.data import datafiles


def player_stats():
    headers = {"User-Agent": "Chrome"}
    url = "https://www.basketball-reference.com/leagues/NBA_2024_ratings.html"

    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")

    tbody = doc.tbody
    trs = tbody.contents

    for tr in trs:
        for td in tr:
            print(td.string)


if __name__ == "__main__":
    player_stats()

