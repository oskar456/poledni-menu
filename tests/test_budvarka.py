import pytest
from poledni_menu.extractors import budvarka


@pytest.mark.vcr()
def test_get_menu():
    menu = list(budvarka.get_menu())
    print(menu)
    assert len(menu) > 5
