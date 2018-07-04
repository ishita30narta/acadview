import sqlite3
conn = sqlite3.connect('projects.db')
print("DATABASE TABLES")

#conn.execute('''CREATE TABLE BOOKS
#            (BOOK_ID  INT PRIMARY KEY  NOT NULL,
#             TITLE_ID  INT   NOT NULL,
#             LOCATION  CHAR(20),
#             GENRE    CHAR(20))''')
#print("Table created successfully")

#conn.execute('''CREATE TABLE TITLES
#            (TITLE_ID  INT PRIMARY KEY  NOT NULL,
#             TITLE  CHAR(20),
#             ISBN  INT  NOT NULL,
#             PUBLISHER_ID  INT  NOT NULL,
#             PUBLISHER_YEAR  INT  NOT NULL)''')
#print("Table created successfully")

#conn.execute('''CREATE TABLE PUBLISHERS
#             (PUBLISHERS_ID  INT PRIMARY KEY  NOT NULL,
#             NAME  TEXT   NOT NULL,
#             STREET_ADDRESS  CHAR(50),
#             SUITE_NUMBER  INT  NOT NULL,
#             ZIP_CODE_ID  INT  NOT NULL)''')
#print("Table created successfully")


#conn.execute('''CREATE TABLE ZIPCODES
#             (ZIP_CODE_ID  INT PRIMARY KEY  NOT NULL,
#             CITY  CHAR(20),
#             STATE  CHAR(20),
#             ZIP_CODE  INT  NOT NULL)''')
#print("Table created successfully")


#conn.execute('''CREATE TABLE AUTHOR_TITLES
#            (AUTHOR_TITLE_ID  INT PRIMARY KEY  NOT NULL,
#             AUTHOR_ID  INT  NOT NULL,
#             TITLE_ID  INT  NOT NULL)''')
#print("Table created successfully")


#conn.execute('''CREATE TABLE AUTHORS
#             (AUTHOR_ID  INT PRIMARY KEY  NOT NULL,
#             FIRST_NAME  TEXT  NOT NULL,
#             MIDDLE_NAME  TEXT  NOT NULL,
#             LAST_NAME  TEXT  NOT NULL)''')
#print("Table created successfully")


#conn.execute("INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(8179922324,976,'California','Comedy')")
#conn.execute("INSERT INTO TITLES(TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR)VALUES(1234,'Monkey Mind',7654,987,2018)")
#conn.execute("INSERT INTO PUBLISHERS(PUBLISHERS_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIP_CODE_ID)VALUES(81097,'ROBIN SHARMA','California',684,100)")
#conn.execute("INSERT INTO ZIPCODES(ZIP_CODE_ID,CITY,STATE,ZIP_CODE)VALUES(22324,'Chandigarh','Chandigarh',888)")
#conn.execute("INSERT INTO AUTHOR_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID)VALUES(1111,666,555)")
#conn.execute("INSERT INTO AUTHORS(AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME)VALUES(444,'Fiyaz','Alli','Khan')")


cursor = conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE from BOOKS")
for row in cursor:
   print("BOOK_ID =",row[0])
   print("TITLE_ID =",row[1])
   print("LOCATION =",row[2])
   print("GENRE =",row[3],"\n")

cursor = conn.execute("SELECT TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLISHER_YEAR from TITLES")
for row in cursor:
   print("TITLES_ID =",row[0])
   print("TITLE =",row[1])
   print("ISBN =",row[2])
   print("PUBLISHER_ID =",row[3])
   print("PUBLISHER_YEAR =", row[4],"\n")


cursor = conn.execute("SELECT PUBLISHERS_ID,NAME,STREET_ADDRESS,SUITE_NUMBER,ZIP_CODE_ID from PUBLISHERS")
for row in cursor:
   print("PUBLISHERS_ID =",row[0])
   print("NAME =",row[1])
   print("STREET_ADDRESS =",row[2])
   print("SUITE_NUMBER =", row[2])
   print("ZIP_CODE_ID =",row[4],"\n")


cursor = conn.execute("SELECT ZIP_CODE_ID,CITY,STATE,ZIP_CODE from ZIPCODES")
for row in cursor:
   print("ZIP_CODE_ID =",row[0])
   print("CITY =",row[1])
   print("STATE =",row[2])
   print("ZIP_CODE =",row[3],"\n")

cursor = conn.execute("SELECT AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID from AUTHOR_TITLES")
for row in cursor:
   print("AUTHOR_TITLE_ID =",row[0])
   print("AUTHOR_ID =",row[1])
   print("TITLE_ID =",row[2],"\n")

cursor = conn.execute("SELECT AUTHOR_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME from AUTHORS")
for row in cursor:
   print("AUTHOR_ID =",row[0])
   print("FIRST_NAME =",row[1])
   print("MIDDLE_NAME =",row[2])
   print("LAST_NAME =",row[3],"\n")

#2

#conn.execute("INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE)VALUES(77,543,'LONDON','Tragedy')")

#conn.commit()
#print("Table created successfully")
#conn.close()


#3

#conn.execute("UPDATE BOOKS set GENRE='xyz' where BOOK_ID =8179922324")
#print("THE ORIGINAL VALUE IS COMEDY")
#print("THE UPDATION VALUE IS XYZ")
cursor = conn.execute("SELECT BOOK_ID,TITLE_ID,LOCATION,GENRE from BOOKS")
for row in cursor:
   print("BOOK_ID =",row[0])
   print("TITLE_ID =",row[1])
   print("LOCATION =",row[2])
   print("GENRE =",row[3],"\n")

conn.commit()
print("Total number of rows update :",conn.total_changes)
conn.close()