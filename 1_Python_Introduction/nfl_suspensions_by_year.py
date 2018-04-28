import csv

f = open("nfl_suspensions_data.csv")
csvreader = csv.reader(f)
nfl_suspensions = list(csvreader)
del nfl_suspensions[0]

years = {}
for i in nfl_suspensions:
	row_year = i[5] 
	if row_year in years:
		years[row_year] += 1
	else:
		years[row_year] = 1
print(years)





teams = [i[1] for i in nfl_suspensions]
unique_teams = set(teams)

games = [i[2] for i in nfl_suspensions]
unique_games = set(games)

print(unique_teams, unique_games)





class Suspension():
	def __init__(self,row):
		self.name = row[0]
		self.team = row[1]
		self.games = row[2]
		try:
			self.year = int(row[5])
		except:
			self.year = 0
	def get_year(self):
	   return self.year

missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
		
