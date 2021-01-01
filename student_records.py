from tkinter import *
from tkinter import messagebox
import student_record_database as st

class student:
    def __init__(self):
        self.main()
        self.rno=0
        
    def load1(self):
        self.rows=st.load()
        self.showdata(0)
        self.rno=0

    def show_all(self):
        self.rows=st.load()
        for row in self.rows:
            self.T1.insert(END, "\n"+str(row))

    def showdata(self, rno):
        self.e1.set(str(self.rows[rno][1]))
        self.e2.set(str(self.rows[rno][2]))
        self.e3.set(str(self.rows[rno][3]))
        

    def add(self):
        self.name=self.e1.get()
        self.roll=self.e2.get()
        self.marks=int(self.e3.get())
        st.add(self.name, self.roll, self.marks)
        self.e1.set(self.name)
        self.e2.set(self.roll)
        self.e3.set(self.marks)

    def delete(self):
        self.roll=self.e2.get()
        st.delete(self.roll)

    def edit(self):
        self.name=self.e1.get()
        self.roll=self.e2.get()
        self.marks=self.e3.get()
        self.id1=self.rows[self.rno][0]
        st.edit(self.name, self.roll, self.marks, self.id1)
        self.e1.set(self.name)
        self.e2.set(self.roll)
        self.e3.set(self.marks)

    def next_record(self):
        if self.rno<len(self.rows):
            self.rno+=1
            self.showdata(self.rno)
        else:
            messagebox.showinfo('Warning', 'It Is Last Record')

    def prev_record(self):
        if self.rno<0:
            messagebox.showinfo('Warning', 'It Is First Record')
        else:
            self.rno-=1
            self.showdata(self.rno)

    def first_record(self):
        self.rno=0
        self.showdata(self.rno)

    def last_record(self):
        last=len(self.rows)
        if self.rno>=last-1:
            messagebox.showinfo('Warning', 'It Is Last Record')
        else:
            self.rno=last-1
            self.showdata(self.rno)

    def main(self):
        root=Tk()
        root.title('Student Records')
        root.geometry('700x550')
        
        self.e1=StringVar()
        self.e2=StringVar()
        self.e3=StringVar()
        self.l=Label(root, text="STUDENT DATABASE MANAGEMENT SYSTEM", fg="red", font="Cambria 24 bold underline")
        self.l.place(x=20, y=20)

        self.T1=Text(root, width=45, height=25, bg="pink")
        self.T1.place(x=300, y=100)
        
        self.l1=Label(root, text="Name : ", font="Cambria 12 bold")
        self.l1.place(x=50, y=100)
        self.E1=Entry(root, textvariable=self.e1, bg="cyan")
        self.E1.place(x=130, y=100)
        
        self.l2=Label(root, text="Roll No. : ", font="Cambria 12 bold")
        self.l2.place(x=50, y=150)
        self.E2=Entry(root, textvariable=self.e2, bg="cyan")
        self.E2.place(x=130, y=150)
        
        self.l3=Label(root, text="Marks : ", font="Cambria 12 bold")
        self.l3.place(x=50, y=200)
        self.E3=Entry(root, textvariable=self.e3, bg="cyan")
        self.E3.place(x=130, y=200)

        self.b1=Button(root, text="Load", bg="yellow", command=self.load1)
        self.b1.place(x=50, y=300)
        self.b1=Button(root, text="First", bg="yellow", command=self.first_record)
        self.b1.place(x=100, y=300)
        self.b1=Button(root, text="Last", bg="yellow", command=self.last_record)
        self.b1.place(x=150, y=300)
        self.b1=Button(root, text="Next", bg="yellow", command=self.next_record)
        self.b1.place(x=200, y=300)
        self.b1=Button(root, text="Prev", bg="yellow", command=self.prev_record)
        self.b1.place(x=250, y=300)
        self.b1=Button(root, text="ADD", bg="yellow", command=self.add)
        self.b1.place(x=100, y=380)
        self.b1=Button(root, text="EDIT", bg="yellow", command=self.edit)
        self.b1.place(x=150, y=380)
        self.b1=Button(root, text="DELETE", bg="yellow", command=self.delete)
        self.b1.place(x=200, y=380)
        self.b1=Button(root, text="Show all", bg="yellow", command=self.show_all)
        self.b1.place(x=120, y=460)
        self.b1=Button(root, text="Exit", fg="white", bg="red", command=root.destroy)
        self.b1.place(x=200, y=460)
        
        root.mainloop()

o1=student()
