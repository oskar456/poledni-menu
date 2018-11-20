import urllib.request
import datetime
import locale

import lxml.html


DEFAULT_PLACE = ""


def get_name(place_id):
    return "Blox"


def get_url(place_id):
    return "http://www.blox-restaurant.cz/#!/page_obedy"


def get_menu(place_id):
    doc = lxml.html.parse(urllib.request.urlopen(get_url(place_id)))
    locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF8')
    dayname = datetime.date.today().strftime("%A")
    rows = doc.xpath(
        '//*[@id="page_obedy"]//*[text() = "{}"]'
        '/ancestor::tr/following-sibling::tr'.format(dayname),
    )
    for meal in rows:
        cols = meal.findall("td")
        if len(cols) == 4:
            num, name, alergens, price = cols
        else:
            continue
        if num.text_content().strip() == "":
            return
        if (name is not None) and (price is not None):
            mealname = name.text_content().strip()
            if mealname:
                yield (mealname, price.text_content().strip())
