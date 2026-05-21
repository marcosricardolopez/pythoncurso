import requests
import urllib3
from bs4 import BeautifulSoup
import csv

# =========================================
# WEB SCRAPING EXAMPLE WITH PYTHON
# =========================================

# Website to scrape
url = "https://news.ycombinator.com"

print("Connecting to website...")
print(f"URL: {url}")

# Download HTML content
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get(url, timeout=10, verify=False)

# Verify request succeeded
if response.status_code != 200:
    print("Error accessing website")
    exit()

print("Website downloaded successfully!")

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all news titles
titles = soup.find_all("span", class_="titleline")

print("\nNews found:\n")
print("=" * 60)

news_list = []

# Extract and display titles
for i, title in enumerate(titles, start=1):
    text = title.get_text()

    print(f"{i}. {text}")

    # Save in list for CSV export
    news_list.append([text])

print("=" * 60)

# =========================================
# EXPORT TO CSV
# =========================================

csv_file = "news_titles.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow(["Title"])

    # Data
    writer.writerows(news_list)

print(f"\nCSV file created successfully: {csv_file}")

# =========================================
# EXTRA INFORMATION
# =========================================

print("\nSummary:")
print(f"Total news extracted: {len(news_list)}")
print("Web scraping completed successfully!")
