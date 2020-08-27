import requests

from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"

res = requests.get(url)

html_icerigi = res.content

soup = BeautifulSoup(html_icerigi,"html.parser")

a = float(input("Rating'i giriniz:"))


basliklar = soup.findAll("td",{"class":"titleColumn"})
ratingler = soup.findAll("td",{"class","ratingColumn imdbRating"})




for baslik, rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) > a):
        print("Film ismi: {} Filmin Ratingi : {}".format(baslik,rating))


