import requests
from bs4 import BeautifulSoup

url = "https://www.tehusetjava.se/category/veckans-te"

headers = {"UserAgent": "Mozzila/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

matching_spans = soup.find_all("span", string="Veckans Te")

for span in matching_spans:
    print("Found:", span)
