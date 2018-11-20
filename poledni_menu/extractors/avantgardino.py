import urllib.request
import datetime

import lxml.html


DEFAULT_PLACE = ""


def get_name(place_id):
    return "Avantgardino"


def get_url(place_id):
    return "http://www.avantgardino.cz/"


def get_menu(place_id):
    doc = lxml.html.parse(urllib.request.urlopen(get_url(place_id)))
    rows = doc.xpath(
        '//div[@class="dennimenu"]'
        '/h3[contains(text(), "{0.day}. {0.month}")]'
        '/../table/tbody/tr'.format(
            datetime.date.today(),
        ),
    )
    for meal in rows:
        cols = meal.findall("td")
        if len(cols) == 3:
            weight, name, price = cols
        else:
            continue
        if (name is not None) and (price is not None):
            mealname = name.text_content().strip().capitalize()
            if mealname:
                yield (mealname, price.text_content().strip())
