import requests
from bs4 import BeautifulSoup

def get_books_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article")

    for book in books:
        title = book.h3.a["title"]
        rating = book.p["class"][-1]  # Get the last word of the class attribute
        print(f"Book titled: {title} has a rating of: {rating} stars")

url = "https://books.toscrape.com/"
get_books_info(url)
