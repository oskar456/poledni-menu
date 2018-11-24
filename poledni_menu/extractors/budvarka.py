import datetime

from ..utils import parsed_html_doc


def get_name():
    return "Budvarka"


def get_url():
    return "https://www.pivnice-budvarka.cz/budvarka-dejvice/"


def get_menu():
    doc = parsed_html_doc(get_url())
    today = datetime.date.today().strftime("%-d.\xa0%-m.\xa0%Y")
    menus = doc.xpath('//div[@id="dnesniMenu"]//'
                      'table/tr'.format(today))
    for meal in menus:
        for pozn in meal.xpath('//span[@class=\"jidelni-nabidka-pozn\"]'):
            pozn.getparent().remove(pozn)
        _, _, _, nazev, cena, _ = (x.text_content()
                                   for x in meal.findall('td'))
        yield (nazev, cena)
