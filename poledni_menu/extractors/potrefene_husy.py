import datetime
import locale

from ..utils import parsed_html_doc


def get_name():
    return "Potrefená husa"


def get_url(place_id='dejvice'):
    return "https://www.potrefene-husy.cz/cz/{}-poledni-menu".format(place_id)


def get_menu():
    doc = parsed_html_doc(get_url())
    locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF8')
    dayname = datetime.date.today().strftime("%A")
    rows = doc.xpath(
        '//*[@id="content-in"]//h3[starts-with(text(), "{}")]'
        '/ancestor::tr/following-sibling::tr'.format(dayname),
    )
    for meal in rows:
        cols = meal.findall("td")
        if len(cols) == 3:
            num, name, price = cols
        else:
            return
        if num.text_content().strip() == "":
            return
        if (name is not None) and (price is not None):
            mealname = name.text_content().strip()
            if mealname:
                yield (mealname, price.text_content().strip())
