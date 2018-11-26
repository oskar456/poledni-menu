import pytest
from poledni_menu.extractors import obedar


@pytest.mark.vcr()
def test_get_menu():
    menu = list(obedar.get_menu())
    print(menu)
    assert len(menu) > 4
