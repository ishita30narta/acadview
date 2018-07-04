import sqlite3
conn = sqlite3.connect('projects.db')
#print("BOOKS")

#conn.execute('''CREATE TABLE BOOK
            # (BOOK_ID  INT PRIMARY KEY  NOT NULL,
             #TITLE_ID  INT   NOT NULL,
             #LOCATION  CHAR(20),
             #GENRE    CHAR(20))''')
#print("Table created successfully")

#conn.execute("INSERT INTO BOOK(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(8179922324,9876,'California','Comedy')")

cursor = conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE from BOOK")
for row in cursor:
   print("BOOK_ID =",row[0])
   print("TITLE_ID =",row[1])
   print("LOCATION =",row[2])
   print("GENRE =",row[3],"\n")


conn.commit()
print("Table created successfully")
conn.close()