import sqlite3
import json

conn=sqlite3.connect('Course&Student_db.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE);
CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE);
CREATE TABLE Member(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER
)''')
#Reading the json file
fname=input('Enter the file')
fhandle=open(fname).read()

js=json.loads(fhandle)
#print(json.dumps(js, indent=4))
print('Number of Entries:', len(js))
count=0
for entry in js:
    name=entry[0]
    course=entry[1]
    role=entry[2]
    print((name , course, role))
    #sql
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name,))
    cur.execute('SELECT id FROM User WHERE name=?',(name,))
    user_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(course,))
    cur.execute('SELECT id FROM Course WHERE title=?',(course,))
    course_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Member (role, user_id, course_id) VALUES (?,?,?)',(role, user_id, course_id))
    count=count+1
conn.commit()
cur.close()
print(count)
print('DONE')
