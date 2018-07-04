import sqlite3
conn = sqlite3.connect('projects.db')
#print("TITLES")

#conn.execute('''CREATE TABLE TITLES
#            (TITLE_ID  INT PRIMARY KEY  NOT NULL,
#             TITLE  CHAR(20),
#             ISBN  INT  NOT NULL,
#             PUBLISHER_ID  INT  NOT NULL,
#             PUBLISHER_YEAR  INT  NOT NULL)''')
#print("Table created successfully")

#conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR)VALUES(12345,'Monkey Mind',7654,987,2018)")

cursor = conn.execute("SELECT TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR from TITLES")
for row in cursor:
   print("TITLES_ID =",row[0])
   print("TITLE =",row[1])
   print("ISBN =",row[2])
   print("PUBLISHER_ID =",row[3])
   print("PUBLISHER_YEAR =", row[4],"\n")

conn.commit()
print("Table created successfully")
conn.close()