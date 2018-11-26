import pytest

from poledni_menu.generate import generate_menu


@pytest.mark.vcr()
def test_generate_menu():
    menu = list(generate_menu("agata"))
    assert menu[0].startswith("[Masarykova kolej](")
    assert menu[1].startswith("----------------")
    assert menu[-1] == ""
    assert len(menu) > 10
