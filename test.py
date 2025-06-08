import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import re

# Define website and conversion rate
url = "https://books.toscrape.com/"
conversion_rate = 157.85  # Example: 1 GBP = 157.85 KES

# Fetch webpage content
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()
    
soup = BeautifulSoup(response.text, 'html.parser')
# Extract book titles and prices
books = []
for book in soup.find_all('article', class_='product_pod')[:10]:
    title = book.h3.a.attrs['title']
    # Extract and clean price
    price_text = book.find('p', class_='price_color').text.strip()
    price_gbp = float(re.sub(r'[^\d.]', '', price_text))  # Remove non-numeric characters
    price_kes = round(price_gbp * conversion_rate, 2)
    books.append({"title": title, "price_GBP": price_gbp, "price_KES": price_kes})
# Store results in CSV/JSON
df = pd.DataFrame(books)
df.to_csv("books_prices.csv", index=False)
with open("books_prices.json", "w") as f:
    json.dump(books, f, indent=4)
# Display results in table format
print(df)
