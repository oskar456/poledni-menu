import string
import urllib.request

import lxml.html


def get_name():
    return "Budvarka"


def get_url():
    return "https://www.budvarkadejvice.cz/denni-menu"


def get_menu():
    # They don't have HTTP-EQUIV meta tag with encoding
    parser = lxml.html.HTMLParser(encoding="utf-8")
    doc = lxml.html.parse(urllib.request.urlopen(get_url()), parser)
    menus = doc.xpath('//div[@class="list-items"]/div[@class="list-item"]')
    for dt in menus:
        name = dt.find('.//a[@class="modify_item"]').text
        name = name.strip()
        price = dt.find('.//span[@class="menu-price"]').text
        allergens = dt.findall('.//span[@class="food-allergens text-xs"]/*')
        al = [ a.text for a in allergens ]
        als = ",".join(al)
        yield ("{} ({})".format(name, als), price)
