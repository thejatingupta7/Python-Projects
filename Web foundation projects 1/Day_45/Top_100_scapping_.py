import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
code = response.text

soup = BeautifulSoup(code, "html.parser")


top_list = []
for movie in soup.find_all(name="h3", class_="title"):
    top_list.insert(0, movie.getText())

with open("top_100_movie.txt", 'a', encoding='utf-8') as f:
    for i in top_list:
        f.write(f"{i}\n")

print(top_list)