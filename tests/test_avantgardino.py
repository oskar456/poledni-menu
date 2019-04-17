from poledni_menu.extractors import avantgardino


def test_get_menu():
    """
    This extractor depends on current date, therefore it fails with the VCR.
    """
    menu = list(avantgardino.get_menu())
    print(menu)
    assert len(menu) > 5
