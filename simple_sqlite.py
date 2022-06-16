import sqlite3
import pandas as pd

conn = sqlite3.connect('SAMPLES.db')

cursor_obj = conn.cursor()

# check if table already exists and delete
cursor_obj.execute("DROP TABLE IF EXISTS SAMPLES")

# create table in database
table = """ CREATE TABLE IF NOT EXISTS SAMPLES (ID INTEGER PRIMARY KEY NOT NULL, GENUSNAME VARCHAR(40), SPECIESNAME VARCHAR(40), ABBREVIATION CHAR(4));"""

try:
	cursor_obj.execute(table)
	print "Table created!"
except:
	"Table could not be created."

# insert rows into table
cursor_obj.execute('''INSERT INTO SAMPLES VALUES (1, 'Latrodectus', 'elegans', 'Lele')''');
cursor_obj.execute('''INSERT INTO SAMPLES VALUES (2, 'Latrodectus', 'hesperus', 'Lhes')''');
cursor_obj.execute('''INSERT INTO SAMPLES VALUES (3, 'Latrodectus', 'mactans', 'Lmac')''');
cursor_obj.execute('''INSERT INTO SAMPLES VALUES (4, 'Latrodectus', 'bishopi', 'Lbis')''');
cursor_obj.execute('''INSERT INTO SAMPLES VALUES (5, 'Latrodectus', 'variolus', 'Lvar')''');

# select and print all rows
statement = ('''SELECT * FROM SAMPLES;''')
cursor_obj.execute(statement)

print "\nFull Table:"
full_output = cursor_obj.fetchall()
for line in full_output:
	print line

# select and print first three rows
cursor_obj.execute(statement)
print "\nPartial Table:"
part_output = cursor_obj.fetchmany(3)
for line in part_output:
	print line

# select and print abbreviations
statement = ('''SELECT ABBREVIATION FROM SAMPLES;''')
col_output = cursor_obj.execute(statement)

print "\nAbbreviations:"
for line in col_output:
	print line

# read data in pandas dataframe
sample_df = pd.read_sql_query("SELECT * FROM SAMPLES;", conn)

print "\nFull Table as dataframe:"
print sample_df
print "Dataframe dimensions", sample_df.shape


# close connection
conn.close()


