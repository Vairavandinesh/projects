import requests
import json
from bs4 import BeautifulSoup
url="http://quotes.toscrape.com"
response=requests.get("http://quotes.toscrape.com")
soup=BeautifulSoup(response.text,"html.parser")
quotes=soup.find_all("div",class_="quote")
quotes_list=[]
for q in quotes:
    text=q.find("span", class_="text").text.strip()
    quotes_list.append(text)
print(quotes_list)
with open("quotes.json","w") as f:
    json.dump(quotes_list,f,indent=2)