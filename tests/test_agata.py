import pytest
from poledni_menu.extractors import agata


@pytest.mark.vcr()
def test_get_name():
    assert agata.get_name() == "Masarykova kolej"
    assert agata.get_name("1") == "Menza Strahov"
    assert agata.get_name("blah") == "Neznámá menza"


@pytest.mark.vcr()
def test_get_menu():
    menu = list(agata.get_menu())
    print(menu)
    assert len(menu) > 5
