import csv

class Team():
	def __init__(self, name):
		self.name = name
		f = open("nfl.csv", 'r')
		csvreader = csv.reader(f)
		self.nfl = list(csvreader)

	def count_total_wins(self):
		count = 0
		for row in self.nfl:
			if row[2] == self.name:
				count = count + 1
		return count
	
	def count_wins_in_year(self, year):
		wins = 0
		for row in self.nfl:
			if row[0] == year and row[2] == self.name:
				wins = wins + 1
		return wins  
	
niners = Team("San Francisco 49ers")
niners_wins_2013 = niners.count_wins_in_year("2013")    