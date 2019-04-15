import pytest
from poledni_menu.extractors import nakotlarce


@pytest.mark.vcr()
def test_get_menu():
    menu = list(nakotlarce.get_menu())
    print(menu)
    assert 5 < len(menu) < 20
