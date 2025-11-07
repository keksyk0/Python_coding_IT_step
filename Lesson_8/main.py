import requests
from bs4 import BeautifulSoup

url = "https://itch.io/"

# Ідентифікуємося як звичайний користувач (щоб сайт не заблокував)
headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/91.0.4472.124'
}


response = requests.get(url, headers=headers)

if response.status_code == 200:
    response.encoding = 'utf-8'
    web = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())

    main_div = web.find("div", class_="featured_game_grid_widget")
    games = main_div.find_all("a", class_="game_cell index_game_cell_widget has_cover")
    for card in games:
        name = card.find("div", class_="label")
        description = card.find("div", class_="sub cell_tags")
        type_price = card.find("div", class_="sub")

        print(name.text.upper())
        print(description.text)
        print(type_price.text)
        print()

else:
    print("Не вдалося завантажити сторінку:", response.status_code)
