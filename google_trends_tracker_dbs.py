import utils
import pytrends
import pandas as pd

from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=['Lewis Hamilton','Daniel Ricardo','Sebastian Vettel'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)

.to_csv()

## JAMIES TASKS

## 1.
# Do some exploratory analysis - Ask some questions then answer them!

## 2.
# Pull all drivers (You can get all drivers names from Kaggle repo)
# Add column with date
# Store to CSV in a Data folder (Make the folder using python HINT: use os liberay)



import os
os.getcwd()
dir(os)


#####################################################################################################################
# EXPLOROTORY ANALYISIS
#####################################################################################################################



################################################
# Q: How countries many have a search history
################################################

# Just filter on Lewis non zero
df[(df['Lewis Hamilton']>0)

# How do i do this on more than 1?
# Filte ron more than one condition on pandas

# Filte ron or (long winded)
df[(df['Lewis Hamilton']>0) | (df['Daniel Ricardo']>0) | (df['Sebastian Vettel']>0)].head()


# Sum across rows and assign new column
df['total_searches'] = df.sum(axis=1)


# Now look at sorted
df.sort_values('total_searches',ascending=False).head()


################################################
# Q: Most popular country per driver
################################################

# Now look at sorted
df.columns[0]
df.sort_values('Lewis Hamilton',ascending=False).head()

# easier way to sort by driver
df.sort_values(df.columns[2],ascending=False).head()


# Filter on non zeor
df[df['total_searches']>0].sort_values('total_searches')


# Sum down the columns
df.sum(axis=0)



df.shape

# bar chart for all geoNames and searches.
%matplotlin inline
df.reset_index().plot(x='geoName', y='Lewis Hamilton', figsize=(120, 30), kind='bar')
