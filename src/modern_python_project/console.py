import textwrap

import click
import requests

from . import __version__, wikipedia


API_URL = "https://{}.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.option('-l',
              '--language',
              default='de',
              help='Language edition of Wikipedia',
              metavar='LANG',
              show_default=True)
@click.version_option(version=__version__)
def main(language):
    """The modern Python project."""
    data = wikipedia.random_page(language=language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))