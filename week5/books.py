import requests
from bs4 import BeautifulSoup
import csv
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =========================================
# WEB SCRAPING PRODUCT PRICES
# =========================================

url = "https://books.toscrape.com"

print("Connecting to website...")

response = requests.get(url, timeout=10, verify=False)

if response.status_code != 200:
    print("Error accessing website")
    exit()

print("Website loaded successfully!")

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all products
products = soup.find_all("article", class_="product_pod")

print("\nProducts Found:\n")
print("=" * 60)

data = []

for product in products:

    # Product name
    title = product.h3.a["title"]

    # Product price
    price = product.find("p", class_="price_color").text

    print(f"Book: {title}")
    print(f"Price: {price}")
    print("-" * 60)

    data.append([title, price])

# =========================================
# SAVE TO CSV
# =========================================

csv_file = "book_prices.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow(["Book", "Price"])

    # Data
    writer.writerows(data)

print(f"\nCSV file created: {csv_file}")

print("\nWeb scraping completed successfully!")