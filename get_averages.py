import sqlite3
db = sqlite3.connect(“discobandit.db”)
cur - db.cursor()
cmd = “SELECT * FROM courses WHERE mark = 80”
sel = cur.execute(cmd) 
for record in sel:
               Print record
