from aux import load_data, remove_subdomains

df = load_data()

df['url'].apply(remove_subdomains)   

# pandas.Series.value_counts method is better alternative to Collections.Counter
domains = df['url'].value_counts()

# print 100 most submitted domains
print(domains[:100])

#for name, row in domains.items():
 #   print("{0}: {1}".format(name, row))



