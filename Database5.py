import sqlite3
conn = sqlite3.connect('projects.db')
#print("AUTHORS TITLES")

#conn.execute('''CREATE TABLE AUTHOR_TITLES
#            (AUTHOR_TITLE_ID  INT PRIMARY KEY  NOT NULL,
#             AUTHOR_ID  CHAR(20),
#             TITLE_ID  CHAR(20))''')
#print("Table created successfully")

#conn.execute("INSERT INTO AUTHOR_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID)VALUES(1111,666,555)")

cursor = conn.execute("SELECT AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID from AUTHOR_TITLES")
for row in cursor:
   print("AUTHOR_TITLE_ID =",row[0])
   print("AUTHOR_ID =",row[1])
   print("TITLE_ID =",row[2],"\n")


conn.commit()
print("Table created successfully")
conn.close()