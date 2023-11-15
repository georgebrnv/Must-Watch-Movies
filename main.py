from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

data = response.text

soup = BeautifulSoup(data, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movie_list = []
for title in titles:
    movie_list.insert(0, title.text)

with open(file="movies.txt", mode="a") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")

