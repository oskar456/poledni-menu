import urllib.request
import lxml.html

DEFAULT_PLACE = "restaurace-praha-dejvice"


def get_name(place_id):
    return "Potrefená husa"


def get_url(place_id):
    return "https://www.potrefene-husy.cz/cz/dejvice-poledni-menu"


def get_menu(place_id):
    """Menu pro Potrefenou Husu"""

    url = "https://www.staropramen.cz/hospody/{}/".format(place_id)
    doc = lxml.html.parse(urllib.request.urlopen(url))
    for meal in doc.xpath(
        '//dt[@class="is-open"]/following-sibling::dd[1]'
        '/ul[@class="menu-list"]/li',
    ):
        name, price = (x.text_content().strip() for x in meal.findall('div'))
        if (name is not None) and (price is not None):
            yield (name, price)
