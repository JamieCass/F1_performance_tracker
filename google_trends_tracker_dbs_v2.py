import utils
import pytrends
import pandas as pd

from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=['Lewis Hamilton','Daniel Ricardo','Sebastian Vettel'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)


type(pytrend)
dir(pytrend)


df_overtime = pytrend.interest_over_time()
df_overtime

import matplotlib as plt
df_overtime.plot(figsize=(20,10))


df_overtime.index

df_overtime_2018 = df_overtime.loc['2018-01-01':'2019-01-01']
df_overtime_2018.plot(figsize=(20,10))



df_overtime_2018

## JAMIES TASKS

## 1.
# Do some exploratory analysis - Ask some questions then answer them!

## 2.
# Pull all drivers (You can get all drivers names from Kaggle repo)
# Add column with date
# Store to CSV in a Data folder (Make the folder using python HINT: use os liberay)

##.to_csv()


import os
os.getcwd()
dir(os)


df.columns

# Total rows in original df
len(df)


# select one column
df['Lewis Hamilton']
len(df['Lewis Hamilton'])

# select one column  - need to feed in a list
df[['Lewis Hamilton','Daniel Ricardo']]
len(df[['Lewis Hamilton','Daniel Ricardo']])

# Same thing
cols = ['Lewis Hamilton','Daniel Ricardo']
df[cols]
len(df[cols])

## SO FAR I HAVE NOT FILTERED ANYTHING


################
# conditions
################
# Sleection on a df - choosing columns, conditions
df[]

df['Lewis Hamilton']>0

# Filter my df if condition = True
df[df['Lewis Hamilton']>0]
df['Lewis Hamilton']>0

# This will not work - we need () for multiple conditions
df[df['Lewis Hamilton']>0 | df['Daniel Ricardo']>0]

# This will work. remember | is "or"
df[(df['Lewis Hamilton']>0) | (df['Daniel Ricardo']>0)]

# Same again this time with 3 conditions
df[(df['Lewis Hamilton']>0) | (df['Daniel Ricardo']>0) | (df['Sebastian Vettel']>0)].head()


# Using brackets to make sure you are clear to python -  what it looks at first is in brackets!
1<5 | 4>1

(1>5) | (4>1)


#  CONDITION               COLUMNS TO RETURN
df[df['Lewis Hamilton']>0]['Lewis Hamilton']


# Sum total for a certain columns

lewis_total = df['Lewis Hamilton'].sum()
ric_total = df['Daniel Ricardo'].sum()
seb_total = df['Sebastian Vettel'].sum()

lewis_total+ric_total+ seb_total


# This sums every columns
df.sum()

# default is asix = 0
df.sum(axis=0)

df.sum(axis=1)

# REMEMBER THIS - UTILIZING PYTHON DOCUMENTATION - WHAT AM I LOOKING AT, WHAT IS INSIDE, HOW DO I USE IT?
type(df)
dir(df)
dir(df.sum)
print(df.sum.__doc__)

def myfunc(x):
    '''
    Explains what function does
    '''
    return x

print(myfunc.__doc__)



df





#####################################################################################################################
# EXPLOROTORY ANALYISIS
#####################################################################################################################



################################################
# Q: How countries many have a search history
################################################

# Just filter on Lewis non zero
df[(df['Lewis Hamilton']>0)]

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

access_key = None
secret_key = None
if (access_key not None) & (secret_key not None):
    print('Yes')

access_key = 1
secret_key = 2
if (access_key is None) & (secret_key is  None):
    print('None')







################################################
# Dictionaries
################################################



myrlq = pytrend.related_queries()
type(myrlq)
myrlq.keys()
type(myrlq)


type(myrlq['Lewis Hamilton'])



# Extract into DF
df_top_related = myrlq['Lewis Hamilton']['top']
df_top_related['type']='top'
df_top_related

df_trising_related = myrlq['Lewis Hamilton']['rising']
df_trising_related['type']='rising'
df_trising_related

# Cobine (union) both dfs into a single df
df_related = pd.concat([df_top_related,df_trising_related])



top_related_final = pd.DataFrame()
for k in myrlq.keys():
    print(k)
    df_top_related = myrlq[k]['top']
    df_top_related['type']='top'
    df_top_related['name']=k
    print(df_top_related.head())
    print('')

    top_related_final = pd.concat([top_related_final,df_top_related])


top_related_final


# Dictionaries
mydict = {'name':'David',
          'age' : 30}

mydict.keys()
mydict.values()

# filter/index a dictionary by keyname
mydict['age']

# Dictionaries
mydict = {'names':{'david':30,
                   'jamie':28},
          'locations':{'david':'TX',
                       'jamie':'PC'}}

mydict['names']
mydict['locations']
