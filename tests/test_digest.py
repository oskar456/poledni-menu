import pytest

from poledni_menu.digest import generate_digest


@pytest.mark.vcr()
def test_generate_digest():
    menu = ["agata", {"extractor": "agata", "place_id": "1"}, ]
    digest = list(generate_digest(menu))
    assert digest[0].startswith("[Masarykova kolej](")
    assert digest[1].startswith("----------------")
    assert digest[-1] == ""
    assert len(digest) > 15
