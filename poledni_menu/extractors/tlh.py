import datetime
import locale

from ..utils import parsed_html_doc


def get_name():
    return "Telehouse Canteen"


def get_url():
    return "https://telehouse-canteen.cz/#!/page_obedy"


def get_menu():
    doc = parsed_html_doc(get_url())
    locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF8')
    dayname = datetime.date.today().strftime("%A")
    rows = doc.xpath(
        '//*[@id="page_obedy"]//*[starts-with(text(), "{}")]'
        '/ancestor::tr/following-sibling::tr'.format(dayname),
    )
    for meal in rows[0:7]:
        cols = meal.findall('td')
        if len(cols) == 4:
            _, name, _, price = cols
        else:
            continue
        if (name is not None) and (price is not None):
            mealname = name.text_content().strip()
            if mealname:
                yield (mealname, price.text_content().strip())
