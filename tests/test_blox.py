import pytest
from poledni_menu.extractors import blox


@pytest.mark.vcr()
def test_get_menu():
    menu = list(blox.get_menu())
    print(menu)
    assert len(menu) > 5
