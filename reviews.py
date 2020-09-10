from requests import get
from bs4 import BeautifulSoup
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

ratings = []
seasons = 17
max_episode_count = 0


def gen_ratings_data():
    for x in range(1, seasons+1):
        url = f'https://www.imdb.com/title/tt1086761/episodes?season={x}&ref_=tt_eps_sn_31'
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        episode_containers = html_soup.find_all('div', {"class": ["list_item even", "list_item odd"]} )
        season_rattings = []
        for x in range(len(episode_containers)):
            episode = episode_containers[x]
            season_rattings.append(str(episode.find('span', class_="ipl-rating-star__rating").text))
        ratings.append(season_rattings)
    for x in range(len(ratings)):
        count = int(len(ratings[x]))
        global max_episode_count
        if count > max_episode_count:
             max_episode_count = count


def gen_csv():
    f = open('numbers2.csv', 'w', newline='')

    with f:
        writer = csv.writer(f)
        for x in range(len(ratings)):
            writer.writerow(ratings[x])


def gen_heatmap():
    #function to crate graph unfinished
    x = []
    y = []

    with open('numbers2.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))

    plt.plot(x, y, label='Loaded from file!')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


gen_ratings_data()
gen_csv()
