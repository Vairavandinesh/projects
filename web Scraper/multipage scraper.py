import requests
from bs4 import BeautifulSoup
import time

base_url = "https://quotes.toscrape.com"
url = "/"

data = []

max_pages = 5   
page_count = 0

while True:
    try:
        response = requests.get(base_url + url)
        response.raise_for_status()
    except Exception as e:
        print("Request failed:", e)
        break

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tags = [tag.text for tag in q.find_all("a", class_="tag")]

        data.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    print(f"Scraped page {page_count + 1}")

    
    next_btn = soup.find("li", class_="next")

    page_count += 1

    if next_btn and page_count < max_pages:
        url = next_btn.find("a")["href"]
        time.sleep(1)   # delay
    else:
        break



print("\nTotal quotes scraped:", len(data))


for item in data[:3]:
    print(item)