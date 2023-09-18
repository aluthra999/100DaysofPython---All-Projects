from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/"
                        "movies/features/best-movies-2/")
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
movie_titles_list = soup.find_all(name="h3", class_="title")

with open("movies.txt", "a", encoding="utf-8") as file:
    for i in reversed(movie_titles_list):
        file.write(i.text + "\n")
