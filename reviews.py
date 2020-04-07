from requests import get
from bs4 import BeautifulSoup
import time
from selenium import webdriver

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


driver = webdriver.Chrome(executable_path=r"C:\Users\Emmett\PycharmProjects\imdb_reviews\drivers\chromedriver.exe")
driver.get(url);
time.sleep(5) # Let the user actually see something!
driver.quit()