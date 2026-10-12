import requests
from bs4 import BeautifulSoup

books_link = "https://books.toscrape.com/"

def scrape_books(scraped_pages, start_page=1, end_page=None):

    books = []
    new_pages = []

    page = start_page
    page_still_valid = True
    reached_end = False

    while page_still_valid:
        if end_page is not None and page > end_page:
            break

        if page in scraped_pages:
            print(f"Page {page} already scraped.")
            page += 1
            continue

        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        try:
            result = requests.get(url, timeout=10)

            if result.status_code == 404:
                print("Reached the last page.")
                reached_end = True
                break


            result.raise_for_status()

            soup = BeautifulSoup(result.text, "lxml")
            book_items = soup.select("article.product_pod")

            if not book_items:
                print(f"No books found on page {page}")
                break

            page_books = []

            for book in book_items:
                title_element = book.select_one("h3 a")
                price_element = book.select_one("p.price_color")
                rating_element = book.select_one("p.star-rating")

                if not title_element or not price_element or not rating_element:
                    raise ValueError(f"Missing book info on page {page}")

                title = title_element.get("title")
                price = price_element.get_text(strip=True).replace("Â", "")
                rating = rating_element.get("class")[1]

                page_books.append({"Title": title, "Price": price, "Rating": rating})
            books.extend(page_books)
            new_pages.append(page)

            print(f"Page {page} scraped.")
            page += 1

        except Exception as error:
            print(f"Error on page {page}: {error}")
            print("Saving successfully scraped pages...")
            page_still_valid = False

    return books, new_pages, reached_end