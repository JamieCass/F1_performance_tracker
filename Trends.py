import pytrends
import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

trend = pytrend.trending_searches('UK')
trend

keywords = pytrend.suggestions(keyword='Mercedes benz')
df = pd.DataFrame(keywords)
df.drop(columns='mid')

pytrend.build_payload(kw_list=['Coronavirus'])
related_queries = pytrend.related_queries()
related_queries.values()

dir(pytrend)

world = pytrend.build_payload(kw_list=['Lewis Hamilton'])
dd = pytrend.interest_by_region()
dd.reset_index().plot(x='geoName', y='Lewis Hamilton', figsize=(120, 10), kind='bar')
