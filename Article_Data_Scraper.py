import requests
from bs4 import BeautifulSoup
import csv

# Define the URL to scrape
url = "https://edition.cnn.com/europe/live-news/russia-ukraine-war-news-04-29-23/h_7394d39de8d2ab399abaece575568715"

# Define the criteria for data extraction
criteria = "article"

# Define the CSV file path and columns
csv_path = "data.csv"
csv_columns = ["Title", "Date", "Author"]

# Send a request to the website and get the response
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the data based on the defined criteria
articles = soup.select(criteria)

# Create a CSV file and write the data to it
with open(csv_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for article in articles:
        title = article.select_one("h2").text
        date = article.select_one("span")
        if date:
            date = date.text
        else:
            date = "UNKNOWN"
        author = article.select_one("p")
        if author:
            author = author.text
        else:
            author = "UNKNOWN"
        writer.writerow({"Title": title, "Date": date, "Author": author})