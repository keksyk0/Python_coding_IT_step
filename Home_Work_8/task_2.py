import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/91.0.4472.124'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response.encoding = 'utf-8'
    web = BeautifulSoup(response.text, "html.parser")

    main_div = web.find("div", class_="col-sm-8 col-md-9")
    books = main_div.find_all("article", class_="product_pod")

    for card in books:
        title_tag = card.h3.a
        price_tag = card.find("p", class_="price_color")

        title = title_tag["title"]
        price = price_tag.text

        print('Title -- ', title)
        print('Price -- ', price)

else:
    print("Не вдалося завантажити сторінку:", response.status_code)
