import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"

data = []

page_number = 1

while True:

    if page_number == 1:
        url = base_url
    else:
        url = base_url + f"catalogue/page-{page_number}.html"

    print(f"Scraping page {page_number}...")

    response = requests.get(url)

    if response.status_code != 200:
        print("No more pages.")
        break

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    if not books:
        break

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text

        price = price.encode("latin1").decode("utf-8")

        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        product_url = urljoin(
            url,
            book.h3.a["href"]
        )

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product URL": product_url
        })

    page_number += 1


df = pd.DataFrame(data)

# Convert price from text to numeric
df["Price"] = df["Price"].str.replace("£", "", regex=False).astype(float)

# Convert rating words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Remove duplicate records
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

# Save cleaned data
df.to_csv("books.csv", index=False)

print("\nData cleaning completed!")
print("Total books:", len(df))
print("\nData types:")
print(df.dtypes)
print("\n--- DATA ANALYSIS ---")

print("\nTotal number of books:")
print(len(df))

print("\nAverage price:")
print(df["Price"].mean())

print("\nHighest price:")
print(df["Price"].max())

print("\nLowest price:")
print(df["Price"].min())

print("\nAverage rating:")
print(df["Rating"].mean())

print("\nBooks by rating:")
print(df["Rating"].value_counts().sort_index())

import matplotlib.pyplot as plt

# Graph 1: Distribution of book prices
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=15, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# Graph 2: Number of books by rating
rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index, rating_counts.values)
plt.title("Number of Books by Rating")
plt.xlabel("Rating (1 to 5)")
plt.ylabel("Number of Books")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig("books_by_rating.png")
plt.show()

print("Graphs saved successfully!")