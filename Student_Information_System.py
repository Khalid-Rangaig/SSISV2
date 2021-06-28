from tkinter import *
import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("Students.db")
    except:
        print("Error")
    return conn    


def verifier():
    a=b=c=d=e=0
    if not student_name.get():
        t1.insert(END,"\n")
        a=1
    if not id_number.get():
        t1.insert(END,"\n")
        b=1
    if not year_level.get():
        t1.insert(END,"\n")
        c=1
    if not gender.get():
        t1.insert(END,"\n")
        d=1
    if not courseID.get():
        t1.insert(END,"\n")
        e=1
    
    if a==1 or b==1 or c==1 or d==1 or e==1:
        return 1
    else:
        return 0


def add_student():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS students(NAME TEXT,ID_NUMBER TEXT,YEAR_LEVEL TEXT,GENDER TEXT,COURSEID TEXT)")
                cur.execute("insert into students values(?,?,?,?,?)",(student_name.get(),id_number.get(),year_level.get(),(gender.get()),courseID.get()))
                conn.commit()
                conn.close()
                t1.insert(END,"DONE\n")


def list_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from students")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM students WHERE ID_NUMBER=?",(id_number.get(),))
        conn.commit()
        conn.close()
        t1.insert(END,"THE STUDENT HAS BEEN DELETED\n")

def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE students SET NAME=?,ID_NUMBER=?,YEAR_LEVEL=?,GENDER=?,COURSEID=? where ID_NUMBER=?",(student_name.get(),id_number.get(),year_level.get(),(gender.get()),(courseID.get()),id_number.get()))
        conn.commit()
        conn.close()
        t1.insert(END,"THE STUDENT HAS BEEN UPDATED\n")

def close():
    sys.exit()



 


if __name__=="__main__":
    root=Tk()
    root.title("Simple Student Management System 2")
    root.geometry("1400x700+0+0",)
    root.config(bg="Red1")

    title = Label(root, text="Simple Student Information System", bd=0, relief=GROOVE,
                      font=("Calibri", 50, "bold italic"), fg="Black",bg="Red1")
    title.pack(side=TOP)
    
     
    student_name=StringVar()
    id_number=StringVar()
    year_level=StringVar()
    gender=StringVar()
    courseID=StringVar()
    
    #======label&entries============
    label1=Label(root,text="Name:",fg="black",bg="Red1",font=("Calibri", 20, "bold italic"))
    label1.place(x=10,y=100)

    e1=Entry(root,textvariable=student_name,font=("Calibri", 16, ), bd=1, relief=GROOVE)
    e1.place(x=150,y=105)

    label2=Label(root,text="ID number:",fg="black",bg="Red1",font=("Calibri", 20, "bold italic"))
    label2.place(x=10,y=160)

    e2=Entry(root,textvariable=id_number,font=("Calibri", 16, ), bd=1, relief=GROOVE)
    e2.place(x=150,y=165)

    label3=Label(root,text="Year Level:",fg="black",bg="Red1",font=("Calibri", 20, "bold italic"))
    label3.place(x=10,y=220)

    e3=Entry(root,textvariable=year_level,font=("Calibri", 16, ), bd=1, relief=GROOVE)
    e3.place(x=150,y=225)

    label4=Label(root,text="Gender:",fg="black",bg="Red1",font=("Calibri", 20, "bold italic"))
    label4.place(x=10,y=280)

    e4=Entry(root,textvariable=gender,font=("Calibri", 16, ), bd=1, relief=GROOVE)
    e4.place(x=150,y=285)

    label5=Label(root,text="CourseID:",fg="black",bg="Red1",font=("Calibri", 20, "bold italic"))
    label5.place(x=10,y=340)

    e5=Entry(root,textvariable=courseID,font=("Calibri", 16, ), bd=1, relief=GROOVE)
    e5.place(x=150,y=345)

    
    #========Table========
    t1=Text(root,width=80,height=20,bd=4)
    t1.place(x=500, y=90, width=795, height=555)

    #======Buttons======
    b1=Button(root,text="ADD STUDENT",bg="Black", fg="white", width=27,height=2,command=add_student)
    b1.place(x=20,y=500)

    b2=Button(root,text="VIEW ALL STUDENTS",bg="Black", fg="white", width=27,height=2,command=list_student)
    b2.place(x=225,y=500)

    b3=Button(root,text="DELETE STUDENT",bg="Black", fg="white", width=27,height=2,command=delete_student)
    b3.place(x=20,y=545)

    b4=Button(root,text="UPDATE INFO",bg="Black", fg="white", width=27,height=2,command=update_student)
    b4.place(x=225,y=545)

   

   

    


    root.mainloop()
