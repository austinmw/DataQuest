
# wildcard: .
strings = ["bat", "robotics", "megabyte"]
regex = ""
regex = "b.t"
 
# beginning: ^a
strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = ""
regex = "^b.tter"

# ending: a$



#askreddit data set
import csv
f = open("askreddit_2015.csv", 'r')
csvreader = csv.reader(f)
posts_with_header = list(csvreader)
posts = posts_with_header[1:]
for post in posts[:10]:
	print(post)



import re

# count "of Reddit" in posts
of_reddit_count = 0
for row in posts:
	if re.search("of Reddit", row[0]) is not None:  #regex,search_in
		of_reddit_count += 1
	
# using square brackets [] to match multiple characters
of_reddit_count = 0
for row in posts:
	if re.search("of [Rr]eddit", row[0]) is not None:
		of_reddit_count += 1
	
	
# escaping special characters
import re
serious_count = 0
# regex = "\.$" end in period
regex = "\[Serious\]"
for row in posts:
	if re.search(regex, row[0]) is not None:
		serious_count += 1
	

# s or S with escaped brackets
import re
serious_count = 0
for row in posts:
	if re.search("\[[Ss]erious\]", row[0]) is not None:
		serious_count += 1
	
	
	
# more complicated example, | or, [] multiple chars 
import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
for row in posts:
	if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) is not None:
		serious_start_count += 1
	if re.search("[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
		serious_end_count += 1
	if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
		serious_count_final += 1
	
	
# substituting regex strings
# re.sub()
import re
posts_new = []
for row in posts:
	row[0] = re.sub("[\[\(][Ss]erious[\]\)]", "[Serious]", row[0])
	posts_new.append(row)

# easier way to search numbers or letters
# search for years 1000 to 2999 in strings
import re
year_strings = []
for string in strings:
	if re.search("[1-2][0-9]{3}", string) is not None:
		year_strings.append(string)


# return a list of substrings matching regex
# re.findall()
import re
years = re.findall("[1-2][0-9]{3}", years_string)

