import utils
import pytrends
import pandas as pd
import csv

from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=['Lewis Hamilton','Daniel Ricardo','Sebastian Vettel'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)

# bar chart for all geoNames and searches.
df.reset_index().plot(x='geoName', y='Lewis Hamilton', figsize=(120, 10), kind='bar')

# How many countries search for Lewis Hamilton?

df[df['Lewis Hamilton']>0]

lew = df['Lewis Hamilton']>0

ric = df['Daniel Ricardo']>0

lew

ric

df.columns[0]

df['total_searches']= df.sum(axis=1)

df.sort_values('Lewis Hamilton', ascending=False).head()

df[df['total_searches']>0]

df['Lewis Hamilton'].sum()

df['Daniel Ricardo'].sum()

df.sum()

dir(pytrend)

# look at interest over time between all 3 drivers.
df_overtime = pytrend.interest_over_time()
df_overtime
# plot into a graph.
df_overtime.plot(figsize=(20,10))

# Search for specific time frame.

df_overtime2018 = df_overtime['2018-01-01':'2019-01-01']

# Plot into a graph
df_overtime2018.plot(figsize=(20,10))

# Find the sum of searched during that year.
df_overtime2018.sum()
