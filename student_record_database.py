import mysql.connector as MySQLdb
from tkinter import messagebox

def load():
    con=MySQLdb.connect(
        host="localhost",
        user="root",
        password="swing",
        database="student_records"
    )
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, sname TEXT, sroll TEXT, smarks TEXT)")
    con.commit()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    con.close()
    return rows

def search(user="root", password="swing"):
    con=MySQLdb.connect(
        host="localhost",
        user="root",
        password="swing",
        database="student_records"
    )
    cur=con.cursor()
    cur.execute("SELECT * FROM student WHERE user=? AND password=?",(user, password))
    rows=cur.fetchall()
    con.close()
    return rows

def add(name, roll, marks):
    con=MySQLdb.connect(
        host="localhost",
        user="root",
        password="swing",
        database="student_records"
    )
    cur=con.cursor()
    cur.execute("INSERT INTO student (sname, sroll, smarks) VALUES(%s, %s, %s)",(name, roll, marks))   
    con.commit()
    con.close()
    messagebox.showinfo('Admin', 'Record Added Successfully!!')

def delete(roll):
    con=MySQLdb.connect(
        host="localhost",
        user="root",
        password="swing",
        database="student_records"
    )
    cur=con.cursor()
    cur.execute("DELETE FROM student WHERE sroll=%s",(roll,))   #comma should be there.
    con.commit()
    con.close()
    messagebox.showinfo('Admin', 'Record Deleted Successfully!!')
   
def edit(name, roll, marks, id1):
    con=MySQLdb.connect(
        host="localhost",
        user="root",
        password="swing",
        database="student_records"
    )
    cur=con.cursor()
    m=int(marks)
    cur.execute("UPDATE student set sname=%s, sroll=%s, smarks=%s WHERE id=%s",(name, roll, m, id1))   
    con.commit()
    con.close()
    messagebox.showinfo('Admin', 'Record Updated Successfully!!')
