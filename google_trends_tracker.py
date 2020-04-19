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

vet = df['Sebastian Vettel']>0

df[df['Lewis Hamilton']>0].sum()

df.columns[0]

list(df.axes[1])

#df['total_searches']= df.sum(axis=1)

df.sort_values('total_searches', ascending=False).head()

df[df['total_searches']>0].sum()

df['Lewis Hamilton'].sum()

df['Daniel Ricardo'].sum()

#Same as above but a bit simpler
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

# Sum of all the countries that searched for Lewis Hamilton
lew.sum()

#Get a list of all the countries that searched for Hammi.
lewdf = df[lew]
print(lewdf.axes[0])

# Put all the countries and searches into a bar graph.
lewdf.reset_index().plot(x='geoName', y='Lewis Hamilton', figsize=(20,10), kind='bar')



# Sum of all the countries that searched for Daniel Ricardo
ric.sum()




#Sum of all the countries that searched for Sebastian Vettel
vet.sum()



type(df)

driver_search = pd.DataFrame()
for k in df.keys():
    print(k)
    df_most_searched = df[k]


drivers_new = [d for d in df.keys()]

df_d = df[drivers_new]
df_d.sort_values(df_d.columns[2], ascending=False)
df_d.plot (x = df_d.axes[0], figsize=(20,10))

print(drivers_new)

df.sort_values(df.columns[0], ascending=False)
