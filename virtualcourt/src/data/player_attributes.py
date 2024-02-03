from bs4 import BeautifulSoup
import requests
from virtualcourt.data import datafiles
import json

team_urls = ['https://www.2kratings.com/teams/atlanta-hawks',
             'https://www.2kratings.com/teams/boston-celtics',
             'https://www.2kratings.com/teams/brooklyn-nets',
             'https://www.2kratings.com/teams/charlotte-hornets',
             'https://www.2kratings.com/teams/chicago-bulls',
             'https://www.2kratings.com/teams/cleveland-cavaliers',
             'https://www.2kratings.com/teams/dallas-mavericks',
             'https://www.2kratings.com/teams/denver-nuggets',
             'https://www.2kratings.com/teams/detroit-pistons',
             'https://www.2kratings.com/teams/golden-state-warriors',
             'https://www.2kratings.com/teams/houston-rockets',
             'https://www.2kratings.com/teams/indiana-pacers',
             'https://www.2kratings.com/teams/los-angeles-clippers',
             'https://www.2kratings.com/teams/los-angeles-lakers',
             'https://www.2kratings.com/teams/memphis-grizzlies',
             'https://www.2kratings.com/teams/miami-heat',
             'https://www.2kratings.com/teams/milwaukee-bucks',
             'https://www.2kratings.com/teams/minnesota-timberwolves',
             'https://www.2kratings.com/teams/new-orleans-pelicans',
             'https://www.2kratings.com/teams/new-york-knicks',
             'https://www.2kratings.com/teams/oklahoma-city-thunder',
             'https://www.2kratings.com/teams/orlando-magic',
             'https://www.2kratings.com/teams/philadelphia-76ers',
             'https://www.2kratings.com/teams/phoenix-suns',
             'https://www.2kratings.com/teams/portland-trail-blazers',
             'https://www.2kratings.com/teams/sacramento-kings',
             'https://www.2kratings.com/teams/san-antonio-spurs',
             'https://www.2kratings.com/teams/toronto-raptors',
             'https://www.2kratings.com/teams/utah-jazz',
             'https://www.2kratings.com/teams/washington-wizards']


def get_roster_url():
    headers = {"User-Agent": "Chrome"}
    roster_url = []

    for team_url in team_urls:
        url = team_url

        result = requests.get(url, headers=headers)
        doc = BeautifulSoup(result.text, "html.parser")

        tbody = doc.tbody
        trs = tbody

        for tr in trs.contents:
            for td in tr:
                for link in td.findAll("span", {"class": "entry-font ml-1"}):
                    for entry in link.findAll('a'):
                        roster_url.append(entry.get("href"))

    return roster_url


def get_player_ratings():
    headers = {"User-Agent": "Chrome"}
    roster_url = get_roster_url()
    team_attr = {}

    for player_url in roster_url:
        url = player_url

        result = requests.get(url, headers=headers)
        doc = BeautifulSoup(result.text, "html.parser")

        rating = doc.findAll("li", {"class": "mb-1"})
        a_list = []

        for container in rating:
            a_list.append(container.get_text())

        idef = a_list[26][0:19]
        a_list[26] = idef

        team_attr.update({player_url: a_list})

    print(team_attr)

    datafile = datafiles.player_attributes()
    open(datafile, "w").write(json.dumps(team_attr, indent=4))


if __name__ == "__main__":
    get_player_ratings()
