import requests
from bs4 import BeautifulSoup

base_url = "https://www.tehusetjava.se"
veckans_url = base_url + "/category/veckans-te"

headers = {"UserAgent": "Mozzila/5.0"}
response = requests.get(veckans_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

list_items = soup.find_all("li", class_="gallery-item")

for li_item in list_items:
    anchor_tag = li_item.find("a", class_="gallery-info-link")

    if anchor_tag:
        veckans_te_span = anchor_tag.find("span", string="Veckans te")

        if veckans_te_span:
            product_title_h3 = anchor_tag.find("h3")
            if product_title_h3:
                title_text = product_title_h3.get_text(strip=True)
                link = base_url + str(anchor_tag.get("href"))
                print(
                    "Found Product Title: {title}, Link: {link}".format(
                        title=title_text, link=link
                    )
                )
            else:
                print("No <h3> tag found within this product link.")
        else:
            pass
    else:
        print("No appropriate <a> tag found in this <li> item.")
