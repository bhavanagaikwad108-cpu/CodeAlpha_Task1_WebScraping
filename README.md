# CodeAlpha Task 1 – Web Scraping

## Project Overview

This project was developed as part of the CodeAlpha Data Analytics Internship.

The project focuses on web scraping book information from the practice website Books to Scrape using Python.

## Objective

The main objective is to collect book-related information from multiple web pages, clean the data, perform basic analysis, and visualize the results.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib

## Data Collected

The following information was collected:

- Book Title
- Price
- Rating
- Availability
- Product URL

## Data Processing

The scraped data was cleaned by:

- Converting prices into numeric values
- Converting ratings into numerical values
- Removing duplicate records
- Resetting the DataFrame index

## Data Analysis

The project calculates:

- Total number of books
- Average book price
- Highest book price
- Lowest book price
- Average rating
- Number of books for each rating

## Data Visualization

The following visualizations were created:

1. Distribution of Book Prices
2. Number of Books by Rating
3. Average Book Price by Rating

## Output Files

- `scraper.py` – Python scraping and analysis code
- `books.csv` – Scraped and cleaned dataset
- `price_distribution.png` – Price distribution chart
- `books_by_rating.png` – Rating distribution chart
- `average_price_by_rating.png` – Average price by rating chart

## Conclusion

The project demonstrates how Python can be used to collect data from websites, clean and analyze the collected data, and create meaningful visualizations.

## Internship

**CodeAlpha Data Analytics Internship**

**Task:** Web Scraping