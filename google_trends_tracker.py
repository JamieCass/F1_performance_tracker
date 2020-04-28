import utils
import pytrends
import pandas as pd
import csv
from pytrends.request import TrendReq
import time
import datetime



##############################################################
# Time and Date code
##############################################################

datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')

DATE = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%y')

DATE


##############################################################
# pytrend and driver list
##############################################################

pytrend = TrendReq()
driver_list = ['Lewis Hamilton','Valtteri Bottas','Sebastian Vettel','Charles Leclerc','Pierre Gasly','Max Verstappen','Daniel Ricardo','Nico Hulkenberg','Romain Grosjean','Kevin Magnussen','Lando Norris','Carlos Sainz','Sergio Perez','Lance Stroll','Kimi Raikkonen','Antonio Giovinazzi','Alexander Albon','Daniil Kvyat','George Russel','Robert Kubica']

def trackerfunc(driver_list, verbose=1):
    '''
    This function looks into what F1 drivers get searched in which reason and how often.

    params
    ---------
    driver_list:list of drivers
    '''
    if verbose>1:
        print('Starting trackerfunc')
    total_drivers = len(driver_list)
    # Number of times we need to loop over
    max_google_request = 5
    iter = int(total_drivers/max_google_request)
    # Difference we need to add every time
    diff = int(total_drivers/iter)
    # Set an empty df
    full_results_region = pd.DataFrame()
    counter = 0
    for i in range(iter):
        pytrend = TrendReq()
        iter_drivers = driver_list[counter:counter+diff]
        #print('COMPLETE:',iter_drivers)
        counter+=diff
        time.sleep(10)
        try:
            pytrend.build_payload(kw_list=iter_drivers)
            df_region = pytrend.interest_by_region()
            ## Can add other things to the payload
            #df_interest_over_time = pytrend.interest_over_time()
            # APPEND TO FULL RESULTS
            full_results_region = full_results_region.append(df_region.T)
            full_results_region['datetime'] = DATE
            print('full_results len',len(full_results_region))
            # CHECK
            print('COMPLETE:',iter_drivers)
        except:
            print ('ERROR',len(iter_drivers))
        # SAVE
        # full_results_region.to_csv('full_results_region.csv',index=False)
    return full_results_region


##############################################################
# Lets see if it works
##############################################################

trackerfunc(driver_list, verbose=1)




full_results_overtime = full_results_overtime.append(df_interest_over_time)
df_interest_over_time.drop(['isPartial'], axis=1)


##############################################################
# save driver list to csv.
##############################################################

pd.DataFrame(driver_list,columns=['driver_name']).to_csv('full_driver_list.csv')
print(pd.read_csv.__doc__)
pd.read_csv('driver_new.csv',header=None)

##################################################
# SHOWING JOINS
##################################################

pytrend.build_payload(kw_list=driver_list[0:0+diff])
df_interest_over_time_A = pytrend.interest_over_time().drop(['isPartial'],axis=1)
df_interest_over_time_A.head()
pytrend.build_payload(kw_list=driver_list[5:5+diff])
df_interest_over_time_B = pytrend.interest_over_time().drop(['isPartial'],axis=1)
df_interest_over_time_B.head()
# Join them instead of transpose and append
# df_joined = pd.merge(df_interest_over_time_A, df_interest_over_time_B, left_on='colname', right_on='colname', how='inner')
df_joined = pd.merge(df_interest_over_time_A, df_interest_over_time_B, left_index=True, right_index=True, how='inner')
df_joined.head()
# Check they are the same length
len(df_interest_over_time_A), len(df_interest_over_time_B)


##############################################################
# other way of doing it
##############################################################

groupkeywords = list(zip(*[iter(driver_list)]*1))
groupkeywords = [list(x) for x in groupkeywords]

dicti = {}
dic_overtime = {}
i = 1
for trending in groupkeywords[0:2]:
	pytrend.build_payload(kw_list=trending)
	print(trending)
	dicti[i] = pytrend.interest_by_region()
	dic_overtime[i] = pytrend.interest_over_time().drop(['isPartial'],axis=1)
	i+=1

dicti[1]



##############################################################
# pytrend and team list
##############################################################

teamtrend = TrendReq()
teamtrend.build_payload(kw_list=['Mercedes','Ferrari','Red Bull','Renault'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)

construstors=teamtrend.interest_by_region()
construstors.plot(figsize=(20,10))


##############################################################
# Lewis Hamilton
##############################################################

# How many countries search for Lewis Hamilton?

#bar chart for all geoNames and searches.
df.reset_index().plot(x='geoName', y='Lewis Hamilton', figsize=(120, 10), kind='bar')


df[df['Lewis Hamilton']>0]

df[df['Lewis Hamilton']>0].sum()

df['Lewis Hamilton'].sum()

lew = df['Lewis Hamilton']>0

#Get a list of all the countries that searched for Hammi.

lewdf = df[lew]
print(lewdf.axes[0])

# Sum of all the countries that searched for Lewis Hamilton
lew.sum()

# Put all the countries and searches into a bar graph.
lewdf.reset_index().plot(x='geoName', y='Lewis Hamilton', figsize=(20,10))

# this shows us that hammi was searched a lot after his win in Abu Dhabi and rosberg still won!
df_overtime.sort_values('Lewis Hamilton', ascending=False)

# this graph pretty much show the searches peak everytime hammi won the chamionship.
df_overtime.plot( y='Lewis Hamilton', figsize=(20,10))



##############################################################
# Daniel Ricardo
##############################################################

ric = df['Daniel Ricardo']>0

# Sum of all the countries that searched for Daniel Ricardo
ric.sum()

##############################################################
# Sebastian Vettel
##############################################################

vet = df['Sebastian Vettel']>0

#Sum of all the countries that searched for Sebastian Vettel
vet.sum()

##############################################################
# Max Verstappen
##############################################################

max = df['Max Verstappen']>0
maxdf = df[max]

maxdf.axes[0]
maxdf.reset_index().plot(x='geoName', y='Max Verstappen', figsize=(20,10))

maxdf.plot(figsize=(20,10))

df['Max Verstappen'].sum()



##############################################################
# Play around area to see if stuff works and see what it does.
##############################################################

df.columns[0]

list(df.axes[1])

#df['total_searches']= df.sum(axis=1)

df.sort_values('total_searches', ascending=False).head()

df[df['total_searches']>0].sum()



df['Daniel Ricardo'].sum()


#Same as above but a bit simpler
df.sum()

dir(pytrend)

# look at interest over time between all 5 drivers.
pytrend.build_payload(kw_list=, timeframe='now 7-d')

df_overtime = pytrend.interest_over_time()
df_overtime

# we can see max verstappen was searched a lot after his first win in Spain!!
df_overtime.sort_values('Max Verstappen', ascending=False)
# plot into a graph.
df_overtime.plot(figsize=(20,10))

# Search for specific time frame.


##############################################################
# Hammi vs Max stuff
##############################################################

df_overtime2018 = df_overtime['2018-01-01':'2019-01-01']

ham_max = df_overtime[['Max Verstappen', 'Lewis Hamilton']]

#Graph to show hammi and max searches from 2015 onwards.
ham_max.plot(figsize=(20,10))

ham_max_overtime = df_overtime2018[['Max Verstappen','Lewis Hamilton']]

#Graph showing just max and hammi searches in 2018
ham_max_overtime.plot(figsize=(20,10))

# max got searched a lot after getting 2nd at Brazil and also when he won at Austria.
df_overtime2018.sort_values('Max Verstappen', ascending=False)
# Plot into a graph
df_overtime2018.plot(figsize=(20,10))

# Find the sum of searched during that year.
df_overtime2018.sum()


##############################################################
# All drivers graph and other bits
##############################################################

type(df)

driver_search = pd.DataFrame()
for k in df.keys():
    print(k)
    df_most_searched = df[k]


drivers_new = [d for d in df.keys()]

df_d = df[drivers_new]
df_d.sort_values(df_d.columns[4], ascending=False)
df_d.plot (figsize=(20,10))

print(drivers_new)

df.sort_values(df.columns[0], ascending=False)
