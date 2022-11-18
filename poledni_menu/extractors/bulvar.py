import datetime
import locale

from ..utils import parsed_html_doc


def get_name():
    return "Restaurace Dejvický Bulvár"


def get_url(place_id='dejvice'):
    return "https://www.restaurace-bulvar.cz/cz/{}-poledni-menu".format(place_id)


def get_menu():
    doc = parsed_html_doc(get_url())
    locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF8')
    dayname = datetime.date.today().strftime("%A")
    rows = doc.xpath('//div[starts-with(@id, "vrmenusection")]')
    
    for row in rows:
        if row.xpath('.//div[@class="vrmenu-detailssectionsub"]/div[@class="vrmenu-detailssectionsubdesc"]/h3/text()')[0] == dayname:
            meals = row.xpath('.//div[contains(@class, "vr-menudetailsprodsubnamedesc")]//h3/text()')
            prices = row.xpath('.//span[contains(@class, "vrmenu-detailsprodsubpricesp")]/text()')

    for name, price  in zip(meals, prices):
        if (name is not None) and (price is not None):
            mealname = name.strip()
            if mealname:
                yield (mealname, price.strip())
