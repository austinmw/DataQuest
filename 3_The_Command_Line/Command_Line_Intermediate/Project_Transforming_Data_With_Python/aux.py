def load_data():
	import pandas as pd
	df = pd.read_csv('hn_stories.csv')
	df.columns = ['submission_time', 'upvotes','url','headline']
	print('data loaded')
	return df    

def remove_subdomains(s):
	s = str(s)
	if len(s.split('.')) > 2:
		l = s.split('.')
		if l[-1] == 'uk':
			s = '.'.join(l[-3:])
		else:
			s = '.'.join(l[-2:])			
		
def extract_hour(s):
	from dateutil.parser import parse
	dt = parse(s)
	return dt.hour
	