import urllib.request
import lxml.html

from ..utils import killwhitespace

_BASE_URL = "https://agata.suz.cvut.cz/jidelnicky/index.php?clPodsystem={}"

_PLACES = {
    "1": "Menza Strahov",
    "2": "Menza Studentský dům",
    "3": "Technická menza",
    "4": "Menza Podolí",
    "5": "Masarykova kolej",
    "10": "Pizzerie la fontanella",
}

DEFAULT_PLACE = "5"


def get_name(place_id):
    return _PLACES.get(str(place_id), "Neznámá menza")


def get_url(place_id):
    return _BASE_URL.format(place_id)


def get_menu(place_id):
    doc = lxml.html.parse(urllib.request.urlopen(get_url(place_id)))

    for meal in doc.findall(
        '//div[@id="jidelnicek"]/div[@class="data"]'
        '/table//tr',
    ):
        tds = meal.findall('td')
        if len(tds) == 0:
            continue
        name = tds[1].text
        price = tds[5].text
        place = tds[6].text_content()
        name, price, place = (killwhitespace(s) for s in (name, price, place))
        if name is "" or name is ".":
            continue
        if place:
            name = "{} ({})".format(name, place)
        yield (name, price)
