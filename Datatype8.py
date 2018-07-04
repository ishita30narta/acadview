import sqlite3
conn = sqlite3.connect('abc.db')

#print("UPDATE")

#conn.execute('''CREATE TABLE UPDATE_VALUES
#             (ID INT PRIMARY KEY   NOT NULL,
#             NAME       TEXT       NOT NULL,
#             AGE        INT        NOT NULL,
#             SALARY     REAL)''')
#print("Table created successfully")


#conn.execute("INSERT INTO UPDATE_VALUES(ID,NAME,AGE,SALARY)VALUES(111,'Ishita',20,60000.00)")
#conn.execute("INSERT INTO UPDATE_VALUES(ID,NAME,AGE,SALARY)VALUES(222,'abc',21,50000.0)")
conn.execute("UPDATE UPDATE_VALUES set SALARY=40000.0 where ID =222")
print(SALARY)
cursor = conn.execute("SELECT ID,NAME,AGE,SALARY from UPDATE_VALUES")
for row in cursor:
    print("ID =",row[0])
    print("NAME =",row[1])
    print("AGE =",row[2])
    print("SALARY =",row[3],"\n")
#conn.commit()
#print("Records inserted successfully")
#conn.close()

print("Total number of rows update :",conn.total_changes)
conn.close()