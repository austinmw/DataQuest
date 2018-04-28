# Takes command line argument of csv file name, prints header and returns dataframe 
# example: python read.py data/hn_stories.csv

def load_data(filename):
	import pandas as pd
	df = pd.read_csv(filename)
	df.columns = ['submission_time', 'upvotes','url','headline']
	print(df.head(3))
	return df    

if __name__ == "__main__":
		# This will call load_data if you run the script from the command line.
	import sys
	load_data(sys.argv[1])
