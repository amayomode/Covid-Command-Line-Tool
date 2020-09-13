import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Data csv urls
data_csv = {
    'confirmed': "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
    'recovered': "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv",
    'deaths': "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
}


def sentence(sent): return sent[0].upper() + sent[1:]


def plot(df, case, country):
    """Plot's time series data"""
    melted_df = df.melt(id_vars=["Country/Region"])
    melted_df.rename(columns={"variable": "Date",
                              "value": 'Numbers'}, inplace=True)

    # plot data
    ax = melted_df.plot(x='Date', y='Numbers')
    ax.set_ylabel('Number of Cases')
    if case != 'deaths':
        case += ' Cases'
    ax.set_title('Total {} In {}'.format(sentence(case), sentence(country)))
    plt.show()


class TimeSeriesPloTs:
    """Methods to plot time series data"""
    @staticmethod
    def plot_country(case, country):

        confirmed_df = pd.read_csv(data_csv[case])

        # prepare country's data frame
        country_data = confirmed_df[confirmed_df['Country/Region'] == country]
        if country_data.empty:
            raise Exception(
                "Country not found\nCheck your spelling or use the proper shortform e.g USA or UK")
        country_data = country_data.drop(
            columns=['Province/State', 'Lat', 'Long'])
        country_data = country_data.groupby('Country/Region').sum()
        country_data['Country/Region'] = country

        plot(country_data, case, country)

    @staticmethod
    def plot_global(case):
        global_df = pd.read_csv(data_csv[case])
        global_df['Country/Region'] = 'Global'

        global_df = global_df.drop(columns=['Province/State', 'Lat', 'Long'])
        global_df = global_df.groupby('Country/Region').sum()
        global_df['Country/Region'] = 'Global'

        plot(global_df, case, country='The World')
