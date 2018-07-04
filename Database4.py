import sqlite3
conn = sqlite3.connect('projects.db')

#print("ZIPCODES")

#conn.execute('''CREATE TABLE ZIPCODES
#             (ZIP_CODE_ID  INT PRIMARY KEY  NOT NULL,
#             CITY  CHAR(20),
#             STATE  CHAR(20),
#             ZIP_CODE  INT  NOT NULL)''')
#print("Table created successfully")
conn.execute("INSERT INTO ZIPCODES(ZIP_CODE_ID,CITY,STATE,ZIP_CODE)VALUES(22324,'Chandigarh','Chandigarh',888)")

cursor = conn.execute("SELECT ZIP_CODE_ID,CITY,STATE,ZIP_CODE from ZIPCODES")
for row in cursor:
   print("ZIP_CODE_ID =",row[0])
   print("CITY =",row[1])
   print("STATE =",row[2])
   print("ZIP_CODE =",row[3],"\n")


conn.commit()
print("Table created successfully")
conn.close()