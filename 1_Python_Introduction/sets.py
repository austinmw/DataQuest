gender = []
for i in legislators:
	gender.append(i[3])
gender = set(gender)
print(gender)




# using set with list comprehension
teams = [i[1] for i in nfl_suspensions]
unique_teams = set(teams)

games = [i[2] for i in nfl_suspensions]
unique_games = set(games)

print(unique_teams, unique_games)