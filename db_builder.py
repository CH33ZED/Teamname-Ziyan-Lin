import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"


c.execute(q)    #run SQL query


csvfile = open('peeps.csv')
reader = csv.DictReader(csvfile)
for row in reader:
             c.execute("INSERT INTO students VALUES('" + row['name'] + "'," + row['age']+ ',' + row['id']+ ')')
#    c.execute("SELECT * FROM students")



q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"


c.execute(q)

csvfile = open('courses.csv')
reader = csv.DictReader(csvfile)
for row in reader:
             c.execute("INSERT INTO courses VALUES('" + row['code'] + "'," + row['mark']+ ',' + row['id'] + ')')


#==========================================================
db.commit() #save changes
db.close()  #close database


