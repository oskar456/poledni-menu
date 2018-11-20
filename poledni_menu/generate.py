

import importlib

import click


def generate_menu(
    extractor, place_id=None,
    override_name=None, override_url=None, **kwargs
):
    """
    Call given extractor. Generate series of Markdown lines with
    menu of given restaurant. Catch and ignore any keyword arguments.
    Catch most exceptions, write them nicely.
    """
    try:
        e = importlib.import_module(".extractors." + extractor, __package__)
        v = place_id or e.DEFAULT_PLACE
        name = override_name or e.get_name(v)
        url = override_url or e.get_url(v)
        title = "[{name}]({url})".format(name=name, url=url)
        yield title
        yield "-"*len(title)
        yield ""
        for meal, price in e.get_menu(v):
            yield "*  {meal} {price}". format(meal=meal, price=price)
    except ImportError as err:
        yield "Cannot import {extractor}: {err}".format(
            extractor=extractor, err=err,
        )
    except (AttributeError, ValueError) as err:
        yield "Error: {err}".format(err=err)
    yield ""


@click.command()
@click.option("--place-id", "-i", help="Extractor-specific place ID")
@click.argument("extractor")
def print_menu(extractor, place_id):
    """
    Print daily menu for a place identified by an extractor and
    optional extractor-dependent place_id.
    """
    for line in generate_menu(extractor, place_id):
        print(line)
