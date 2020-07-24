import sqlite3

conn=sqlite3.connect('orgCount_db.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (
                        org TEXT,
                        count INTEGER)''')
fname=input('Enter the file name-\n')
fhandle=open(fname)
for line in fhandle:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    words=line.split()
    pieces=words[1].split('@')
    org=pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org=?',(org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=? ',(org,))
conn.commit()
sqllstr='SELECT org,count FROM Counts ORDER BY count DESC LIMIT 5'
for row in cur.execute(sqllstr):
    print(row[0],row[1])
cur.close()
