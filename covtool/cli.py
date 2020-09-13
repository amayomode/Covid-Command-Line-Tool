import click
from covtool import dataset
from pyfiglet import Figlet
from covtool import plot_time_series
from click_help_colors import HelpColorsGroup, HelpColorsCommand


import warnings
warnings.filterwarnings("ignore")

data = dataset.DataSet()


def pretty_print(data, json=False):
    if json:
        click.echo(data)
    else:
        for k, v in data.items():
            if not v:
                v = 'N/A'
            click.echo(click.style(k, fg='blue', bold='True') + ': ' +
                       click.style(v, fg='yellow', bold=True))


@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="green"
)
@click.version_option('0.1.0', prog_name='covcli_tools')
def cli():
    pass


@cli.command('get')
@click.option('-w', '--world', is_flag=True, help="Get World-Wide Covid Numbers")
@click.option('-j', '--json', is_flag=True, help="Print the Data in Json Format")
@click.option('-c', '--country', help="Get a Country's Covid Numbers")
def get(world, country, json):
    """
    Get Covid Data
    e.g covtool get --world or
    covtool get --country USA 
    """
    if world:
        dt = data.get_global_data()
        pretty_print(dt, json)
    if country:
        dt = data.get_country_data(country)
        pretty_print(dt, json)


@cli.command("plot-global")
@click.argument(
    'type', default='confirmed',
    type=click.Choice(['recovered', 'confirmed', 'deaths'])
)
def plot_global(type):
    """
    Plot Global Time Series Plot by catergory i.e recovered|confirmed|deaths
    e.g covtool plot-global confirmed 
    """
    click.echo(click.style(
        "Generating Plot....", fg='cyan', bold='true'))
    plot_time_series.TimeSeriesPloTs.plot_global(type)
    click.echo(click.style(
        "Done....", fg='green', bold='true'))


@cli.command("plot-country")
@click.option('-n', '--name', required=True, help="Name of the Country")
@click.argument(
    'case', default='confirmed',
    type=click.Choice(['recovered', 'confirmed', 'deaths'])
)
def plot_country(name, case):
    """
    Plot Country's Time Series Plot by catergory i.e recovered|confirmed|deaths
    e.g covtool plot-county -n US recovered
    """
    click.echo(click.style(
        "Generating Plot....", fg='cyan', bold='true'))
    plot_time_series.TimeSeriesPloTs.plot_country(case, name)
    click.echo(click.style(
        "Done....", fg='green', bold='true'))


@cli.command("update", help="Update Locally Cached Data")
def update():
    """Updates Cached Dataset"""
    click.echo(click.style(
        "Updating....", fg='cyan', bold='true'))

    data.update_data()
    click.echo(click.style(
        "Cached Data Sucessfully updated", fg='blue', bold='true'))


@cli.command("info")
def info():
    """Information About The Tool"""
    f = Figlet(font='standard')
    click.echo(f.renderText('covtool'))
    click.secho(
        "covtool: a simple CLI for fetching covid data", fg='cyan')
    click.echo(
        "Data Sources: https://www.worldometers.info/coronavirus\nJohn Hopkins [https://github.com/CSSEGISandData/COVID-19] ")
    click.secho("Author: Amayo II <amayomordecai@gmail.com>", fg='magenta')


def main():
    cli()
