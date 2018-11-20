import urllib.request
import datetime

import lxml.html

DEFAULT_PLACE = "na-kotlarce"


def get_name(place_id):
    return "Bernard Pub Na Kotlářce"


def get_url(place_id):
    return "https://www.bernardpub.cz/pub/" + place_id


def get_menu(place_id):
    doc = lxml.html.parse(urllib.request.urlopen(get_url(place_id)))
    tabs = doc.xpath(
        '//section[@class="daily-menu"]'
        '//ul[@class="day-selection"]/li'
        '/span[text()="{0.day}. {0.month}."]/..'.format(
            datetime.date.today(),
        ),
    )
    if len(tabs) < 1:
        raise ValueError("Na dnešek není vystaveno menu")

    dm = doc.findall('//div[@id="{}"]//div[@class="single-food"]'.format(
        tabs[0].get('data-tab-target'),
    ))
    for meal in dm:
        name = meal.find('strong')
        price = meal.find('span[@class="food-price"]')
        if (name is not None) and (price is not None):
            mealname = name.text_content().strip().capitalize()
            if mealname:
                yield (mealname, price.text_content().strip())
