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

