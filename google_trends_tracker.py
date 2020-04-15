import utils
import pytrends
import pandas as pd

from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=['Lewis Hamilton','Daniel Ricardo'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)

# bar chart for all geoNames and searches.
df.reset_index().plot(x='geoName', y='Lewis Hamilton', figsize=(120, 10), kind='bar')

# How many countries search for Lewis Hamilton?

lew = df['Lewis Hamilton']>0

ric = df['Daniel Ricardo']>0

lew

ric

df.columns[0]

df['total_searches']= df.sum(axis=1)

df.sort_values(df.columns[0], ascending=False).head()
df[df['total_searches']>0]
