from fetch_data import fetch_data, get_time_diff
from pathlib import Path
import pandas as pd
import os

# path
path, filename = os.path.split(os.path.realpath(__file__))


class DataSet:
    """Dataset Class. Fetches scrapes covid data from worldometers.info"""

    def __init__(self):
        if not os.path.isfile(os.path.join(path, "data/covid_data.ft")):
            fetch_data()

        self.dataset = pd.read_feather(
            os.path.join(path, "data/covid_data.ft"))

        get_time_diff()

    def get_global_data(self):
        """Returns Global Statisctics"""
        return {k: v for k, v in zip(self.dataset.columns[2:], self.dataset.loc[0][1:])}

    def get_country_data(self, country):
        """
        Returns Country's Specific Data
        :param country: name of country to fetch data from
        """
        country = country[0].upper() + country[1:]
        index = self.dataset.loc[self.dataset["Country,Other"] == country]['#']
        if index.empty:
            return "Country not found\nCheck your spelling or use the proper shortform e.g USA or UK"

        return {k: v for k, v in zip(self.dataset.columns[2:], self.dataset.loc[int(index)][2:])}

    def download_data(self, name='covid_dataset.csv', directory=str(Path.home())):
        """
        Saves the dataset in CSV format
        :param name: name of how you want to save the dataset
        :param directory: directory where you want to save the file
        """
        if not name.endswith('.csv'):
            return "Invalid File Name. File should end with .csv for example dataset.csv"
        try:
            self.dataset.to_csv(os.path.join(directory, name))
            return f"Saved Dataset {name} to {directory}"
        except Exception as e:
            return e.message, e.args

    def update_data(self):
        fetch_data()


if __name__ == "__main__":
    dataset = DataSet()
    print(dataset.get_global_data())
    print(dataset.get_country_data("Kenya"))
