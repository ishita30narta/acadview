import sqlite3
conn = sqlite3.connect('test.db')
print("opened database successfully")

#conn.execute('''CREATE TABLE COMPANY
            # (ID INT PRIMARY KEY   NOT NULL,
            # NAME       TEXT       NOT NULL,
            # AGE        INT        NOT NULL,
            # ADDRESS    CHAR(50),
            # SALARY     REAL)''')
#print("Table created successfully")

#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)VALUES(3,'Paul',32,'California',20000.00)")
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)VALUES(4,'Allen',25,'Texas',15000.00)")
#conn.execute("UPDATE COMPANY set SALARY=25000.00 where ID = 1")
conn.execute("DELETE from COMPANY where ID = 2")conn.commit()


cursor = conn.execute("SELECT ID,NAME,ADDRESS,SALARY from COMPANY")#where salary is greater than 10000
for row in cursor:
    print("ID =",row[0])
    print("NAME =",row[1])
    print("ADDRESS =",row[2])
    print("SALARY =",row[3],"\n")
#conn.commit()
#print("Records created successfully")
#print("Operation done successfully")


print("Total number of rows update :",conn.total_changes)
conn.close()