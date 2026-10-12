from books_scraper import scrape_books
from movie_scraper import scrape_movies
from file_handler import save_data
from summary import print_summary, session_summary

def main():
    session = []
    scraped_pages = set()
    books_finished = False
    movies_scraped = False

    while True:
        print("_________________________")
        print("MULTI-WEBSITE WEB SCRAPER")
        print("_________________________")
        print("1. Scrape Books")
        print("2. Scrape Movies")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            while True:
                print("BOOKS SCRAPER\n")
                print("1. Scrape all pages")
                print("2. Scrape selected pages")
                print("3. Back to main menu")

                books_choice = input("Enter choice: ")

                if books_choice == "3":
                    break

                if books_choice not in ("1", "2"):
                    print("Invalid input")
                    continue

                if books_finished:
                    print("All pages were scraped in this session")
                    continue

                start_page = 1
                end_page = None

                if books_choice == "2":
                    try:
                        start_page = int(input("Enter starting page: "))
                        end_page = int(input("Enter ending page: "))

                        if start_page < 1 or end_page < start_page:
                            print("Invalid page range.")
                            continue
                    except ValueError:
                        print("Please enter valid page numbers.")
                        continue

                print("Scraping Books...")

                data,new_pages,reached_end = scrape_books(scraped_pages,start_page,end_page)

                if not data:
                    print("No new books to scrape.")
                    continue

                try:
                    file_path = save_data(data, "books")
                    scraped_pages.update(new_pages)

                    if reached_end and books_choice == "1":
                        books_finished = True

                    data_types = ["Book title", "Price", "Rating"]

                    print_summary("Books to Scrape", data, data_types, file_path)

                    session.append({"website": "Books to scrape",
                                    "file": file_path,
                                    "records": len(data),
                                    "data_types":data_types
                                    })

                except Exception as error:
                    print(f"Error saving books: {error}")

        elif choice == "2":
            if movies_scraped:
                print("Movies have already been scraped in this session.")
                continue
            try:
                print("Scraping Movies...")
                data = scrape_movies()

                if not data:
                    print("No movies found")
                    continue

                file_path = save_data(data, "movies")
                movies_scraped = True
                data_types = ["Movie title", "Director", "Country"]
                print_summary("Wikipedia - Action Films of the 2020s", data, data_types, file_path)
                session.append({"website": "Wikipedia - Action Films of the 2020s",
                                "file": file_path,
                                "records": len(data),
                                "data_types": data_types})

            except Exception as error:
                print(f"Error: {error}")

        elif choice == "3":
            session_summary(session)
            break

        else:
            print("Invalid choice. Please choose 1,2 or 3.")

if __name__ == "__main__":
    main()





