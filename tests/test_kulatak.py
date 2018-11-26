import pytest
from poledni_menu.extractors import kulatak


@pytest.mark.vcr()
def test_get_menu():
    menu = list(kulatak.get_menu())
    print(menu)
    assert len(menu) > 3
