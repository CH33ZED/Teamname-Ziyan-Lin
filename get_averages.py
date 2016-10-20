import sqlite3
db = sqlite3.connect("discobandit.db")
c = db.cursor()

def avg():
  u = 0
  b = ""
  while (u < 11):
      cmd = "SELECT id FROM courses WHERE mark = %s;" %(u)
      sel = c.execute(cmd)
      total = 0;
      num = 0;
      for a in sel:
          num += 1
          total += a[0]
      if(num != 0):
        ccd = "SELECT name FROM students WHERE id = %s;" %(u)
        joe = c.execute(ccd)
        x = ""
        for d in joe:
            x = d[0]
        print "Name: " + x + " ID:" + str(u) + " Average:" + str(total/num)
      u = u + 1



avg()
c.close
db.close()
