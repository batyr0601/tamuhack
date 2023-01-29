# pull inflation, unemployment, and interest rate data from the Federal Reserve
import fredapi as fred
import pandas as pd
import datetime as dt

# create a fred object
api = fred.Fred(api_key='b36625b35aa1f0c091fa73a67fb49e12')

start = dt.date(2020, 1, 1)
end = dt.date.today()

inflation = api.get_series('CORESTICKM159SFRBATL', observation_start=start, observation_end=end)
unemployment = api.get_series('UNRATE', observation_start=start, observation_end=end)
interest = api.get_series('DFF', observation_start=start, observation_end=end)

def get_from_last_month():
    return inflation[-1], unemployment[-1], interest[-1]


