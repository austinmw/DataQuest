import sqlite3

conn = sqlite3.connect("factbook.db")

query = "select name from facts order by population asc limit 10"
print(conn.execute(query).fetchall())

