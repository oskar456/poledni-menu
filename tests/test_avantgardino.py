import pytest
from poledni_menu.extractors import avantgardino


@pytest.mark.vcr()
def test_get_menu():
    menu = list(avantgardino.get_menu())
    print(menu)
    assert len(menu) > 5
