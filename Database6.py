import sqlite3
conn = sqlite3.connect('projects.db')

#print("AUTHORS")

#conn.execute('''CREATE TABLE AUTHORS
#             (AUTHOR_ID  INT PRIMARY KEY  NOT NULL,
#             FIRST_NAME  TEXT  NOT NULL,
#             MIDDLE_NAME  TEXT  NOT NULL,
#             LAST_NAME  TEXT  NOT NULL)''')
#print("Table created successfully")
#conn.execute("INSERT INTO AUTHORS(AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME)VALUES(444,'Fiyaz','Alli','Khan')")

cursor = conn.execute("SELECT AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME from AUTHORS")
for row in cursor:
   print("AUTHOR_ID =",row[0])
   print("FIRST_NAME =",row[1])
   print("MIDDLE_NAME =",row[2])
   print("LAST_NAME =",row[3],"\n")


conn.commit()
print("Table created successfully")
conn.close()