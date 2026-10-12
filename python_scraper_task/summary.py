def print_summary(website,data,data_types, file_path):
    print("SCRAPING COMPLETE SUCCESSFULLY")
    print(f"Website: {website} ")
    print("Data Scraped:")

    for data_type in data_types:
        print(f" - {data_type}")

    print(f"Records collected: {len(data)}")
    print("Data saved to:")
    print(file_path)

def session_summary(session):
    print("SESSION SUMMARY\n")

    if not session:
        print("No websites were scraped.")
    else:
        for operation in session:
            print(f"Website: {operation['website']}")
            print(f"Records: {operation['records']}")
            print(f"File: {operation['file']}")
            print("Data types:")

            for data_type in operation["data_types"]:
                print(f" - {data_type}")

    print("Goodbye!\n")