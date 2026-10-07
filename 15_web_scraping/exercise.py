#____________________________________________
import requests
from bs4 import BeautifulSoup
#Task-grab the authors
result = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(result.text, "lxml")
soup.select(".author")
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
    print(name.text)

#____________________________________________

#Task-grab the quotes
soup = BeautifulSoup(result.text, "lxml")
soup.select(".quote")

quotes = set()
for quote in soup.select(".text"):
    quotes.add(quote.text)
    print(quote.text)

#____________________________________________

#Task-top ten tags

soup = BeautifulSoup(result.text, "lxml")
soup.select(".tag-item")

for item in soup.select(".tag-item"):
    print(item.text)

#____________________________________________

#Task-with the number of pages

link = "http://quotes.toscrape.com/page/"

authors = set()
for page in range(1, 10):
    page_link = link+str(page)
    result = requests.get(page_link)
    soup = BeautifulSoup(result.text, "lxml")

    for name in soup.select(".author"):
        authors.add(name.text)
        print(authors)


#Task-when you don't know the number of pages


link = "http://quotes.toscrape.com/page/"

authors = set()
page = 1

while True:
    page_link = link + str(page)
    result = requests.get(page_link)
    soup = BeautifulSoup(result.text, "lxml")
    quotes = soup.select(".quote")

    if not quotes:
        break

    for name in soup.select(".author"):
        authors.add(name.text)


    page += 1

for name in authors:
    print(name)




