import pytest
from poledni_menu.extractors import potrefene_husy


@pytest.mark.vcr()
def test_get_menu():
    menu = list(potrefene_husy.get_menu())
    print(menu)
    assert len(menu) > 4
