import sqlite3
conn = sqlite3.connect('project.db')
print("BOOKS")
conn.execute('''CREATE TABLE BOOKS
            (ID INT PRIMARY KEY   NOT NULL,
             TITLE_ID   INT       NOT NULL,
             LOCATION   CHAR(50),
             GENRE   TEXT     NOT NULL)''')
#conn.execute("INSERT INTO BOOKS(BOOK-ID,TITLE_ID,LOCATION,GENRE)VALUES(81-7992-232-4,98765,'California','Comedy')")

#cursor = conn.execute("SELECT BOOK-ID,TITLE_ID,LOCATION,GENRE from BOOKS")
#for row in cursor:
 #   print("BOOK-ID =",row[0])
  #  print("TITLE_ID =",row[1])
   # print("LOCATION =",row[2])
    #print("GENRE =",row[3],"\n")

conn.commit()
print("Record updated successfully")
conn.close()