from requests import get
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))


for x in range(len(movie_containers)):
    first_movie = movie_containers[x]
    title = first_movie.h3.a.text
    ratting = first_movie.find('div', class_="inline-block ratings-imdb-rating").strong.text
    print(title + "    " +ratting)
