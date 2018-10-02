import sqlite3

def connect():
    conn=sqlite3.connect("book_selection.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book_selection (id INTEGER PRIMARY KEY, rollno INTEGER, book_id INTEGER)")
    conn.commit()
    conn.close()

def insert(rollno, book_id):
    conn=sqlite3.connect("book_selection.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book_selection VALUES (NULL,?,?)",(rollno, book_id))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("book_selection.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book_selection")
    rows=cur.fetchall()
    conn.close()
    return rows

def selected_bookid_search(roll_no):
    conn=sqlite3.connect("book_selection.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book_selection WHERE rollno =?", (roll_no,))
    rows=cur.fetchall()
    conn.close()
    return rows

def view_selected_books(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE id =? ",(id,))
    rows=cur.fetchall()
    conn.close()
    return rows
    
def delete(id):
    conn=sqlite3.connect("book_selection.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book_selection WHERE book_id=?",(id,))
    conn.commit()
    conn.close()
"""
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()
"""
connect()
#insert(12,32)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
print(view())
#print(search(author="John Smooth"))
for a in selected_bookid_search(15334):
    print(a[2])
