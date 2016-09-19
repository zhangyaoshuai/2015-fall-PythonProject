import operator 
import json
import preprocess as pre
from collections import Counter
from nltk.corpus import stopwords
import string
from nltk import bigrams 
import vincent
import pandas

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
dates_jets = []
fname = 'football.json'
with open(fname, 'r') as f:
    for line in f:
    	tweet = json.loads(line)
        terms_hash = [term for term in pre.preprocess(tweet['text']) if term.startswith('#')]
    	terms_only = [term for term in pre.preprocess(tweet['text']) 
              if term not in stop and
              not term.startswith(('#', '@'))]
        if 'jets' in terms_only:
            dates_jets.append(tweet['created_at'])
    #Print the first 5 most frequent words
    #print(count_all.most_common(10))
# a list of "1" to count the hashtags
ones = [1]*len(dates_jets)
# the index of the series
idx = pandas.DatetimeIndex(dates_jets)
# the actual series (at series of 1s for the moment)
Jets = pandas.Series(ones, index=idx)
 
# Resampling / bucketing
per_minute = Jets.resample('1Min').sum().fillna(0)
time_chart = vincent.Line(Jets)
time_chart.axis_titles(x='Time', y='Freq')
open('time_chart_football.json', 'w').close()
time_chart.to_json('time_chart_football.json')


