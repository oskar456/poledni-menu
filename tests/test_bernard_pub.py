import pytest
from poledni_menu.extractors import bernard_pub


@pytest.mark.vcr()
def test_get_menu():
    menu = list(bernard_pub.get_menu())
    print(menu)
    assert len(menu) > 5
