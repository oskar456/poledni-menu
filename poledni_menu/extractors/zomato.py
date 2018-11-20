import datetime
import html
from pathlib import Path

try:
    import requests
except ImportError:
    raise ValueError("This extractor requires requests package to work")

try:
    p = Path("~/.config/zomatoapikey.txt").expanduser()
    api_key = p.read_text().strip()
except FileNotFoundError:
    raise ValueError("This extractor requires an API key. Obtain one and "
                     "put it to {}.".format(p))


_PLACES = {
    "16505958": ("Pod Loubím", "http://www.podloubim.com/menu/"),
    "18311812": ("Nad Alejí", "http://nadaleji.wixsite.com/nadaleji"),
    "16506914": ("DAP", "http://www.daphotel.cz/"),
}

DEFAULT_PLACE = "18311812"


def get_name(place_id):
    try:
        return _PLACES[place_id][0]
    except KeyError:
        return "Neznámá restarurace"


def get_url(place_id):
    try:
        return _PLACES[place_id][1]
    except KeyError:
        return ""


def get_menu(place_id):
    url = "https://developers.zomato.com/api/v2.1/dailymenu"
    params = {'res_id': place_id}
    headers = {
        'user_key': api_key,
        'Accept': 'application/json',
    }
    req = requests.get(url, headers=headers, params=params)
    doc = req.json()
    dishes = []
    for menu in doc['daily_menus']:
        sd = menu['daily_menu'].get('start_date')
        ed = menu['daily_menu'].get('end_date')
        if sd:
            sd = datetime.datetime.strptime(sd, "%Y-%m-%d %H:%M:%S")
        if ed:
            ed = datetime.datetime.strptime(ed, "%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
        if sd and sd <= now and (not ed or ed > now):
            dishes.extend(menu['daily_menu'].get('dishes'))

    for meal in dishes:
        name, price = (killthatwhitespace(s)
                       for s in [meal['dish']['name'], meal['dish']['price']])
        yield (name, price)


def killthatwhitespace(string):
    return " ".join(html.unescape(s).strip()
                    for s in string.split()).capitalize()
