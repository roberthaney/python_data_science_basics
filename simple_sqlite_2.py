import sqlite3, csv
import pandas as pd

# open link to sqlite db
conn = sqlite3.connect("chicago_socioeconomic.db")
cur = conn.cursor()

# read in remote csv file, store as datafame
df = pd.read_csv("https://data.cityofchicago.org/resource/jcxq-k9xf.csv")
# convert dataframe to sql table
df.to_sql("chicago_socioeconomic_data", conn, if_exists="replace", index=False)

# check table
for row in cur.execute("SELECT * FROM chicago_socioeconomic_data LIMIT 5;"):
	print row

# get number of rows in dataset
print "Number of rows:", cur.execute("SELECT count(*) FROM chicago_socioeconomic_data;").fetchall()[0][0]

# check column names
print cur.execute("SELECT name FROM PRAGMA_TABLE_INFO('chicago_socioeconomic_data');").fetchall()

# check hardship metrics
print "Number of high hardship areas:",cur.execute("SELECT count(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50;").fetchall()[0][0]
print "Highest hardship area:",cur.execute("SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;").fetchall()[0][0]
print "Highest hardship area:",cur.execute("SELECT community_area_name FROM chicago_socioeconomic_data WHERE hardship_index = (SELECT MAX(hardship_index) FROM chicago_socioeconomic_data);").fetchmany(1)[0][0]
print "Per capita > 60k:",cur.execute("SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;").fetchall()

# make dataframe with variables
income_v_hardship = pd.DataFrame(cur.execute("SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;").fetchall())
income_v_hardship.columns = (["per_capita_income", "hardship_index"])



