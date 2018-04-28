
# read and split
data = open("guns.csv", 'r').readlines() 
data_final = []
for row in data:
	data_final.append(row.split(','))

# alternative open: with csv module
import csv
f = open("guns.csv", 'r')
csvreader = csv.reader(f)
data = list(csvreader)
print(data[:5], '\n\n')

# extract header
headers = data[0]
data = data[1:]
print(headers,'\n\n')
print(data[:5], '\n\n')

# count years
years = [row[1] for row in data]
year_counts = {}
for y in years:
	if y not in year_counts:
		year_counts[y] = 1
	else:
		year_counts[y] += 1
print(year_counts, '\n\n')

# create datetime.datetime object with dates
import datetime 
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
print(dates[:5])

# count up how many times each unique date occurs
date_counts = {}
for d in dates:
	if d in date_counts:
		date_counts[d] += 1
	else:
		date_counts[d] = 1
print(date_counts, '\n\n')

# gender and race counts
sexes = [row[5] for row in data]
races = [row[7] for row in data]
sex_counts = {}
race_counts = {}
for s in sexes:
	if s in sex_counts:
		sex_counts[s] += 1
	else:
		sex_counts[s] = 1
for r in races:
	if r in race_counts:
		race_counts[r] += 1
	else:
		race_counts[r] = 1
print(race_counts, '\n\n', sex_counts, '\n\n')

# get census data 
f = open("census.csv")
csvreader = csv.reader(f)
census = list(csvreader)
print(census, '\n\n')

# rate of gun deaths per 100000 for each race
mapping = {}
for r in race_counts:
	mapping[r] = 0	
for row in census[1:]:
	mapping["White"] += int(row[10])
	mapping["Black"] += int(row[12])
	mapping["Asian/Pacific Islander"] += int(row[14])
	mapping["Asian/Pacific Islander"] += int(row[15])
	mapping["Hispanic"] += int(row[11])
	mapping["Native American/Native Alaskan"] += int(row[13])
race_per_hundredk = {}
for k in race_counts:
	race_per_hundredk[k] = (race_counts[k] / mapping[k]) * 100000
print(race_per_hundredk, '\n\n')

# homicide rates by race per 100000
intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_per_hundredk = {}
for i, race in enumerate(races):
	if intents[i] == 'Homicide':
			if race in homicide_race_per_hundredk:
				homicide_race_per_hundredk[race] += 1
			else:
				homicide_race_per_hundredk[race] = 1				
print(homicide_race_per_hundredk, '\n\n')
for k in homicide_race_per_hundredk:
	homicide_race_per_hundredk[k] = (homicide_race_per_hundredk[k] / mapping[k]) * 100000
print(homicide_race_per_hundredk, '\n\n')