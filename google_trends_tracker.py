import utils
import pytrends
import pandas as pd

from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=['Lewis Hamilton'])
# Interest by Region
df = pytrend.interest_by_region()
df.head(10)

# bar chart for all geoNames and searches.
df.reset_index().plot(x='geoName', y='Lewis Hamilton', figsize=(120, 10), kind='bar')
