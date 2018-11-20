import urllib.request
import datetime
import locale

import lxml.html


DEFAULT_PLACE = ""


def get_name(place_id):
    return "Kulaťák"


def get_url(place_id):
    return "https://www.kulatak.cz/"


def get_menu(place_id):
    doc = lxml.html.parse(urllib.request.urlopen(get_url(place_id)))
    locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF8')
    dayname = datetime.date.today().strftime("%A")
    for meal in doc.xpath('//div[@id="daily_menu"]/table/tbody/tr/td'
                          '/strong[contains(.,"{}")]/../..'
                          '/../*'.format(dayname)):
        cells = meal.findall('td')
        if len(cells) != 3:
            continue
        x, name, price = cells
        if (name is not None) and (price is not None):
            yield (name.text_content().strip(), price.text_content().strip())
