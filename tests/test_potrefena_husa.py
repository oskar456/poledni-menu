import pytest
from poledni_menu.extractors import potrefena_husa


@pytest.mark.vcr()
def test_get_menu():
    menu = list(potrefena_husa.get_menu())
    print(menu)
    assert len(menu) > 4
