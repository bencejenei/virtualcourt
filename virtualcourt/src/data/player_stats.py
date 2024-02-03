from bs4 import BeautifulSoup
import requests
import json
from virtualcourt.data import datafiles


def player_stats():
    url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    tbody = doc.tbody
    trs = tbody.contents

    player_card = {}

    for tr in trs:
        try:
            for td in tr.contents[1:]:
                try:
                    player_id = td["data-append-csv"]
                    player_card.update({player_id: {"BR_player_id": td["data-append-csv"]}})
                except:
                    pass
                player_card[player_id].update({td["data-stat"]: td.string})
        except:
            pass

    datafile = datafiles.player_stats()
    open(datafile, "w").write(json.dumps(player_card, indent=4))


if __name__ == "__main__":
    player_stats()
