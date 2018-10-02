import sqlite3

def connect():
	conn = sqlite3.connect("student.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS student_signup(id INTEGER PRIMARY KEY, username TEXT,roll_no INTEGER, mobile_no INTEGER, gender TEXT, password TEXT, confirm_password TEXT)")
	conn.commit()
	conn.close()

def insert(username,roll_no, mobile_no, gender, password, confirm_password):
	conn = sqlite3.connect("student.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO student_signup VALUES (NULL,?,?,?,?,?,?)", (username,roll_no, mobile_no, gender, password, confirm_password))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("student.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM student_signup")
	rows = cur.fetchall()
	conn.close()
	return rows

def update(roll_no, mobile_no, password, confirm_password):
	conn = sqlite3.connect("student.db")
	cur = conn.cursor()
	cur.execute("UPDATE student_signup SET password = ?, confirm_password = ? WHERE roll_no = ? and mobile_no = ?", (password, confirm_password,roll_no, mobile_no) )
	conn.commit()
	conn.close()	

def search(username,password):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student_signup WHERE username=? AND password=? ", (username,password))
    rows=cur.fetchall()
    conn.close()
    return rows[0][2]

def delete(id):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM student_signup WHERE id=?",(id,))
    conn.commit()
    conn.close()

connect()
print(view())

print( search('saahil kumar','hello saahil') )
       
