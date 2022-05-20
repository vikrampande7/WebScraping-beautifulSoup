from bs4 import BeautifulSoup
import requests


URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL2 = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL2)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
#print(soup.prettify())

all_titles = soup.find_all(name="h3", class_="title")
#print(all_titles)
movie_titles = [movie.getText() for movie in all_titles]
movies = movie_titles[::-1]

with open("top100_movies.txt", mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")

""" With FOR loop to reverse
for n in range(len(movie_titles) - 1, -1, -1):
    print(movie_titles[n])"""