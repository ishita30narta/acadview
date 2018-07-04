import sqlite3
conn = sqlite3.connect('projects.db')
#print("PUBLISHERS")

#conn.execute('''CREATE TABLE PUBLISHERS
#             (PUBLISHERS_ID  INT PRIMARY KEY  NOT NULL,
#             NAME  TEXT   NOT NULL,
#             STREET_ADDRESS  CHAR(50),
#             SUITE_NUMBER  INT  NOT NULL,
#             ZIP_CODE_ID  INT  NOT NULL)''')
#print("Table created successfully")

#conn.execute("INSERT INTO PUBLISHERS(PUBLISHERS_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIP_CODE_ID)VALUES(81097,'ROBIN SHARMA','California',684,100)")

cursor = conn.execute("SELECT PUBLISHERS_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIP_CODE_ID from PUBLISHERS")
for row in cursor:
   print("PUBLISHERS_ID =",row[0])
   print("NAME =",row[1])
   print("STREET_ADDRESS =",row[2])
   print("SUITE_NUMBER =", row[2])
   print("ZIP_CODE_ID =",row[4],"\n")


conn.commit()
print("Table created successfully")
conn.close()