import pytest
from poledni_menu.extractors import bulvar


@pytest.mark.vcr()
def test_get_menu():
    menu = list(bulvar.get_menu())
    print(menu)
    assert len(menu) > 3
