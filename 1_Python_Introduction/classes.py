class Car():
	def __init__(self):
		self.color = "black"
		self.make = "honda"
		self.model = "accord"

black_honda_accord = Car()
print(black_honda_accord.color)





class Team():
	def __init__(self):
		self.name = "Tampa Bay Buccaneers"
		
bucs = Team()
print(bucs.name)

class Team2():
	def __init__(self, name):
		self.name = name
		
giants = Team2("New York Giants")
print(giants)



class Suspension():
	def __init__(self,row):
		self.name = row[0]
		self.team = row[1]
		self.games = row[2] 
		self.year = row[5]
		
third_suspension = Suspension(nfl_suspensions[2])




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
		
