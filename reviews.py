from requests import get
from bs4 import BeautifulSoup
import csv
import matplotlib
import matplotlib.pyplot as plt

rattings = []

def gen_ratings_data():
    for x in range(1, 5):
        url = f'https://www.imdb.com/title/tt0096697/episodes?season={x}&ref_=tt_eps_sn_31'
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        episode_containers = html_soup.find_all('div', {"class": ["list_item even", "list_item odd"]} )
        season_rattings = []
        for x in range(len(episode_containers)):
            episode = episode_containers[x]
            season_rattings.append(str(episode.find('span', class_="ipl-rating-star__rating").text))
        rattings.append(season_rattings)


def gen_csv():
    f = open('numbers2.csv', 'w', newline='')

    with f:
        writer = csv.writer(f)
        for x in range(len(rattings)):
            writer.writerow(rattings[x])


def gen_heatmap():
    pass


gen_ratings_data()
gen_csv()
gen_heatmap()