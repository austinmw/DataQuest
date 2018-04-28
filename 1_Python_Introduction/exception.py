
try:
	float("hello")
except Exception:
	print("Error converting to float.")
	
	
try:
	int('')
except Exception as exc:
	print(type(exc))
	print(str(exc))
	
	
converted_years = []
for i in birth_years:
	year = i
	try:
	   year = int(year)
	except Exception:
		pass
	converted_years.append(year)



# add extra column to legislators with birth year
for row in legislators:
	birthday = row[2]
	birth_year = birthday.split("-")[0]
	try:
		birth_year = int(birth_year)
	except Exception:
		birth_year = 0
	row.append(birth_year)
	
	
last_value = 1
for row in legislators:
	if row[7] == 0:
		row[7] = last_value
	last_value = row[7]
		
		
		