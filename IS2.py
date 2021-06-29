from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3


def Database():
    global conn, cursor
    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUDSS (STU_ID INT, STU_NAME TEXT, STU_GENDER TEXT, STU_YEAR TEXT, STU_COURSE TEXT, STU_COURSECODE TEXT)")


def DisplayForm():
    display_screen = Tk()
    display_screen.geometry("1200x600")
    display_screen.resizable(False,False)
    display_screen.title("STUDENT MANAGEMENT SYSTEM")
    global tree
    global SEARCH
    global ID,name,gender,year,course,coursecode
    SEARCH = StringVar()
    ID = StringVar()
    name = StringVar()
    gender = StringVar()
    year = StringVar()
    course = StringVar()
    coursecode = StringVar()
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LFrom = Frame(display_screen, width=350,bg="Red1")
    LFrom.pack(side=LEFT, fill=Y)
    LeftViewForm = Frame(display_screen, width=500,bg="Red1")
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=600,bg="Red1")
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Student Management System", font=('verdana', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    Label(LFrom, text="ID  ", font=("Times New Roman", 12),bg="Red1").pack(side=TOP)
    Entry(LFrom,font=("Calibri",10,"bold"),textvariable=ID).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Name  ", font=("Times New Roman", 12),bg="Red1").pack(side=TOP)
    Entry(LFrom,font=("Calibri",10,"bold"),textvariable=name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Gender ", font=("Times New Roman", 12),bg="Red1").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Year ", font=("Times New Roman", 12),bg="Red1").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"),textvariable=year).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="course ", font=("Times New Roman", 12),bg="Red1").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"),textvariable=course).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="coursecode ", font=("Times New Roman", 12),bg="Red1").pack(side=TOP)
    Entry(LFrom, font=("Calibri", 10, "bold"),textvariable=coursecode).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Add",font=("Calibri", 10, "bold"),bg="Black",fg="White",command=register).pack(side=TOP, padx=10,pady=5, fill=X)

    lbl_txtsearch = Label(LeftViewForm, text="Enter ID to Search", font=('Calibri', 10),bg="RED1",fg="Black")
    lbl_txtsearch.pack()
    
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    
    btn_search = Button(LeftViewForm, text="Search",bg="BLUE",fg="White" ,command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_view = Button(LeftViewForm, text="ViewList",bg="black",fg="White", command=DisplayData)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_reset = Button(LeftViewForm, text="Clear",bg="black",fg="White", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_delete = Button(LeftViewForm, text="Delete",bg="black",fg="White", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
   
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "Name", "Gender", "year","course","coursecode"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    
    tree.heading('Student Id', text="Student Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('year', text="year", anchor=W)
    tree.heading('course', text="course", anchor=W)
    tree.heading('coursecode', text="coursecode", anchor=W)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def register():
    Database()
    
    ID1=ID.get()
    name1=name.get()
    gender1=gender.get()
    year1=year.get()
    course1=course.get()
    coursecode1=coursecode.get()
    
    if ID1=='' or name1=='' or gender1==''or year1=='' or course1==''or coursecode1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        
        conn.execute('INSERT INTO STUDSS (STU_ID,STU_NAME,STU_GENDER,STU_YEAR,STU_COURSE,STU_COURSECODE) \
              VALUES (?,?,?,?,?,?)',(ID1,name1,gender1,year1,course1,coursecode1));
        conn.commit()
        tkMessageBox.showinfo("Message","Added successfully")
        DisplayData()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    ID.set("")
    name.set("")
    gender.set("")
    year.set("")
    course.set("")
    coursecode.set("")
def Delete():
    
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM STUDSS WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def SearchRecord():
    Database()
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor=conn.execute("SELECT * FROM STUDSS WHERE STU_ID LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def DisplayData():
    Database()
    tree.delete(*tree.get_children())
    cursor=conn.execute("SELECT * FROM STUDSS")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


DisplayForm()
if __name__=='__main__':
 mainloop()
