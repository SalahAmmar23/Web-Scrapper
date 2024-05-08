import requests

from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")


for book in books: 
    title = book.h3.a["title"]
    rating = book.p["class"][-1]   # to get the last word  if it's star-rating Three  we only get the three
    print("Book titled: " + title + "has a rating of: " + rating + " stars")

