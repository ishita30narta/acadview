import sqlite3
conn = sqlite3.connect('abc.db')
#print("company")

#conn.execute('''CREATE TABLE COMPANY_DETAILS
#             (ID  INT PRIMARY KEY  NOT NULL,
#             NAME  TEXT   NOT NULL,
#             AGE  INT  NOT NULL,
#             SALARY    REAL)''')
#print("Table created successfully")

#conn.execute("INSERT INTO COMPANY_DETAILS(ID,NAME,AGE,SALARY)VALUES(222,'Zeena',20,50000.0)")

cursor = conn.execute("SELECT ID,NAME,AGE,SALARY from COMPANY_DETAILS")
for row in cursor:
   print("ID =",row[0])
   print("NAME =",row[1])
   print("AGE =",row[2])
   print("SALARY =",row[3],"\n")


conn.commit()
print("Table created successfully")
conn.close()