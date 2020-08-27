import requests
from bs4 import BeautifulSoup
import mysql.connector
baglanti=mysql.connector.connect(use='root',password='',host='127.0.0.1',database='imdb')
isaretci=baglanti.cursor()
url = "http://www.imdb.com/chart/top"

res = requests.get(url)

html_icerigi = res.content

soup = BeautifulSoup(html_icerigi,"html.parser")


basliklar = soup.findAll("td",{"class":"titleColumn"})
ratingler = soup.findAll("td",{"class","ratingColumn imdbRating"})



for baslik, rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")


isaretci.execute('''INSERT INTO filmler (film_adi,film_reyting) SELECT "{0}","{1}" WHERE NOT EXİSTS (SELECT film_adi From filmler WHERE film_adi ="{0}") LIMIT 1 '''.format (baslik))
baglanti.commit()
sonuc=isaretci.execute('''SELECT film_adi,film_reyting FROM filmler ORDER BY film_reyting DESC LIMIT 5 ''')
isaretci.fetchall()
isaretci.close()
baglanti.close()


