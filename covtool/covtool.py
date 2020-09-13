import click
from dataset import DataSet
from pyfiglet import Figlet
from plot_time_series import TimeSeriesPloTs
from click_help_colors import HelpColorsGroup, HelpColorsCommand


import warnings
warnings.filterwarnings("ignore")

data = DataSet()


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
def main():
    pass


@main.command('get')
@click.option('-w', '--world', is_flag=True, help="Get World-Wide Covid Numbers")
@click.option('-j', '--json', is_flag=True, help="Print the Data in Json Format")
@click.option('-c', '--country', help="Get a Country's Covid Numbers")
def get(world, country, json):
    """Get Covid Data"""
    if world:
        dt = data.get_global_data()
        pretty_print(dt, json)
    if country:
        dt = data.get_country_data(country)
        pretty_print(dt, json)


@main.command("plot-global")
@click.argument(
    'type', default='confirmed',
    type=click.Choice(['recovered', 'confirmed', 'deaths'])
)
def plot_global(type):
    """
    Plot Global Time Series Plot by catergory i.e recovered|confirmed|deaths
    e.g covtool plot global confirmed 
    """
    click.echo(click.style(
        "Generating Plot....", fg='cyan', bold='true'))
    TimeSeriesPloTs.plot_global(type)
    click.echo(click.style(
        "Done....", fg='green', bold='true'))


@main.command("plot-country")
@click.option('-n', '--name', required=True, help="Name of the Country")
@click.argument(
    'case', default='confirmed',
    type=click.Choice(['recovered', 'confirmed', 'deaths'])
)
def plot_country(name, case):
    """
    Plot Country's Time Series Plot by catergory i.e recovered|confirmed|deaths
    e.g covtool.py plot county -n US recovered
    """
    click.echo(click.style(
        "Generating Plot....", fg='cyan', bold='true'))
    TimeSeriesPloTs.plot_country(case, name)
    click.echo(click.style(
        "Done....", fg='green', bold='true'))


@main.command("update")
def update():
    """Updates Cached Dataset"""
    click.echo(click.style(
        "Updating....", fg='cyan', bold='true'))

    data.update_data()
    click.echo(click.style(
        "Cached Data Sucessfully updated", fg='blue', bold='true'))


@main.command("info")
def info():
    """Information About The Tool"""
    f = Figlet(font='standard')
    click.echo(f.renderText('covtool'))
    click.secho(
        "covtool: a simple CLI for fetching covid data", fg='cyan')
    click.echo(
        "Data Sources: https://www.worldometers.info/coronavirus\nJohn Hopkins [https://github.com/CSSEGISandData/COVID-19] ")
    click.secho("Author: Amayo II <amayomordecai@gmail.com>", fg='magenta')


if __name__ == "__main__":
    main()
