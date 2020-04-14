GOOGLE TRENDS HELP!!!

# Google trends help.

# ALl help came from https://github.com/Tanu-N-Prabhu/Python/blob/master/Google_Trends_API.ipynb

import pytrends
from pytrends.request import TrendReq
import pandas as pd

pytrend = TrendReq() # this connects to google.

# google hot trends data, daily search trends..
pytrend.trending_searches(pn = 'australia')

# worldwide, you wouldnt put a parameter. so get rid of 'pn'

# todays trending search..
pytrend.today_searches

df = pytrend.trending_searches(pn='united_kingdom')
df


# google keywords suggestions.
keywords = pytrend.suggestions(keyword = 'Mercedes benz')
df_1 = pd.DataFrame(keywords)
df_1.drop(columns = 'mid') # mid column didnt make sense..
