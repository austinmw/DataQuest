# script for printing top 100 words in the headlines of hn_stories data

from aux import load_data # import load data function

df = load_data() # load dataframe
df['headline'] = df['headline'].astype(str) # convert series to strings
hl = df['headline'].tolist() # convert to list
l = ' '.join(hl) # join list to string
print('series joined as string')
words = l.split(' ') # separate by space into words
print('words separated')
words = [w.lower() for w in words]
print('words converted to lowercase')
import collections
c = collections.Counter(words)
top100 = [s[0] for s in c.most_common(100)]

for items in top100:
	print(items)