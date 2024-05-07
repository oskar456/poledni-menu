
from ..utils import parsed_html_doc


def get_name():
    return "Jídlovice TLH"


def get_url():
    return "https://www.jidlovice.cz/telehouse/"

def get_menu():
    doc = parsed_html_doc(get_url())
    rows = doc.xpath("//div[@class='et_pb_row et_pb_row_1']//div[@class='et_pb_text_inner']//*[self::p or self::h4][string-length(normalize-space()) > 0 and not(contains(., '&nbsp;'))]")
    found_start = False
    found_end = False
    for meal in rows:
        text = meal.xpath("string()")
        if "POLÉVKY" in text:
            found_start = True
            continue
        elif "JÍDLOVICKÉ STÁLICE" in text:
            found_end = True
            break
        if found_start and not found_end:
            for line in text.split("Kč"):
               if '|' in line:
                   name, price = line.split('|', 1)
                   yield (name.strip(), price.strip())
