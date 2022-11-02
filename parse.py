import requests
from bs4 import BeautifulSoup

URL = "https://www.kivano.kg/noutbuki?brands=acer-apple"
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "accept": "*/*",
}
LIN = "https://www.kivano.kg"
# responce = requests.get(URL, headers=HEADERS)



def get_html(url, headers):
    responce = requests.get(url, headers=headers)
    return responce


def get_content_from_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    items = soup.find_all("div", class_="item product_listbox oh")
    laptops = []
    for item in items:
        laptops.append(
            {
                "title": item.find("div", class_="listbox_title oh").get_text().replace("\n", ""),
                "discription": item.find("div", class_="product_text pull-left").get_text().replace("\n", ""),
                "price": item.find("div", class_="listbox_price text-center").get_text().replace("\n", ""),
                "image": LIN + item.find("img").get("src"),
            }
        )
    print(laptops)


def get_result_parse():
    html = get_html(URL, HEADERS)
    if html.status_code == 200:
        get_content_from_html(html.text)


get_result_parse()
