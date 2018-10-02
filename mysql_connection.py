import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'demo', user = 'root', password = 'root')
        if conn.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(e)
    finally:
        conn.close()
if __name__ == '__main__':
    connect()

def view():
    try:
        conn = mysql.connector.connect(host = 'localhost', database = 'demo', user = 'root', password = 'root')
        cursor = conn.cursor()
        cursor.execute("SELECT *FROM user_info")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()    
            

def insert(name, password):
    conn = mysql.connector.connect(host = 'localhost', database = 'demo', user = 'root', password = 'root')    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_info VALUES(%s, %s)", (name, password) )
    conn.commit()
    cursor.close()
    conn.close()

view()

def update(name, password, user):
    conn = mysql.connector.connect(host = 'localhost', database = 'demo', user = 'root', password = 'root')
    cursor = conn.cursor()
    cursor.execute("UPDATE user_info SET name = %s , password = %s WHERE name = %s ", (name, password, user) )
    conn.commit()
    cursor.close()
    conn.close()

#update('hello', 'friends','kumar')
#print("---------")
#view()
print("-----------------------------------------------------------------------------------------------")
def delete_row(username):
    conn = mysql.connector.connect(host = 'localhost', database = 'demo', user = 'root', password = 'root')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_info WHERE name = %s ", (username,) )
    conn.commit()
    cursor.close()
    conn.close()
delete_row('udit')
view()

    
    
