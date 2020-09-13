import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from termcolor import colored

# path
path, filename = os.path.split(os.path.realpath(__file__))

time_format = "%d/%m/%Y %H:%M:%S"


def format_time(delta):
    d = {'d': abs(delta.days)}
    d['h'], rem = divmod(delta.seconds, 3600)
    d['m'], d['s'] = divmod(rem, 60)
    return "Using Cached Data Last Fetched {d} days {h} hours, {m} minutes and {s} seconds ago\nTo update run 'covtool.py update'".format(**d)


def set_time():
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime(time_format)
    return dt_string


def get_time_diff():
    with open(os.path.join(path, 'data/time.txt'), 'r') as f:
        last_time = datetime.strptime(f.readline(), time_format)
        time_difference = datetime.now()-last_time
        readable_diff = format_time(time_difference)
        if time_difference.days >= 1:
            print(colored(readable_diff, color='red'))
        else:
            print(colored(readable_diff, color='green'))


def get_page(url):
    """Download Page from a given Url"""
    response = requests.get(url)
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
    return response.content


def fetch_data():
    """Scrapes data from worldometers.info and strores it in a dataframe"""

    page = get_page("https://www.worldometers.info/coronavirus")
    soup = BeautifulSoup(page, 'lxml')
    # Search for the table and extracting its data
    table = soup.find('table', attrs={'id': 'main_table_countries_today'})
    rows = table.find_all("tr", attrs={"style": ""})
    data = []
    for i, item in enumerate(rows):
        if i == 0:
            data.append(item.text.strip().split("\n")[:13])
        else:
            data.append(item.text.strip().split("\n")[:12])

    # save data to a dataframe
    dt = pd.DataFrame(data)
    dt = pd.DataFrame(data[1:], columns=data[0][:12])
    dt.columns = ['#', 'Country,Other', 'TotalCases', 'NewCases', 'TotalDeaths',
                  'NewDeaths', 'TotalRecovered', 'NewRecovered', 'ActiveCases',
                  'Serious,Critical', 'TotalCases/1M pop', 'Deaths/1M pop']

    # strore is as temp file for quick loading
    dt.to_feather(os.path.join(path, 'data/covid_data.ft'))
    # set accession time
    with open(os.path.join(path, 'data/time.txt'), 'w+') as f:
        f.write(set_time())


if __name__ == "__main__":
    get_time_diff()
