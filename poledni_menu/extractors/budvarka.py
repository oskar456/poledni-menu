import urllib.request
import datetime

import lxml.html

DEFAULT_PLACE = ""


def get_name(place_id):
    return "Budvarka"


def get_url(place_id):
    return "https://www.pivnice-budvarka.cz/budvarka-dejvice/"


def get_menu(place_id):
    doc = lxml.html.parse(urllib.request.urlopen(get_url(place_id)))
    today = datetime.date.today().strftime("%-d.\xa0%-m.\xa0%Y")
    menus = doc.xpath('//div[@id="dnesniMenu"]//'
                      'table/tr'.format(today))
    for meal in menus:
        for pozn in meal.xpath('//span[@class=\"jidelni-nabidka-pozn\"]'):
            pozn.getparent().remove(pozn)
        _, _, _, nazev, cena, _ = (x.text_content()
                                   for x in meal.findall('td'))
        yield (nazev, cena)
