from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql

win = Tk()
win.title('Student Management System')
win.config(bg='#cbedf2')
win.geometry('1200x700')
win.resizable(False, False)
mlogo = PhotoImage(file='applogo.png')
win.iconphoto(True, mlogo)

db = ''

def connect():
    global db
    connectbutton.config(state=DISABLED)
    database = Toplevel()
    database.resizable(False, False)
    database.geometry('570x300')
    database.title("Database Connection")
    database.config(bg='#c0f0b9')
    dataframe = Frame(database, bg='#c0f0b9')
    dataframe.place(x=0, y=20)

    def destroy():
        global db
        db = dbentry.get()

        if hostentry.get() == 'localhost' and userentry.get() == 'root' and passentry.get() == 'RPm@#5959' and len(db) != 0:
            try:
                object = sql.connect(host='localhost', user='root', password='RPm@#5959', database=db)
            except:
                messagebox.showerror(title="Error", message='Enter a existing database!')
                database.destroy()
                connectbutton.config(state=NORMAL)
                return ()
            connectbutton.config(text=(db, 'connected'), state=DISABLED)
            addstudent.config(state=NORMAL)
            deletestudent.config(state=NORMAL)
            updatestudent.config(state=NORMAL)
            searchstudent.config(state=NORMAL)
            showstudents.config(state=NORMAL)
            exit.config(state=NORMAL)
            messagebox.showinfo(title="Success", message="Successfully connected!")
            studentable.delete(*studentable.get_children())
            cursor = object.cursor()
            cursor.execute("select * from student")
            datalist = cursor.fetchall()

            for i in datalist:
                studentable.insert('', END, values=i)
        else:
            messagebox.showerror(title="Error", message='Incorrect Input')
            connectbutton.config(state=NORMAL)

        database.destroy()

    hostlabel = Label(dataframe, text='                  Host :', font=('Times New Roman', 20,), padx=15, pady=10,bg='#c0f0b9')
    hostlabel.grid(row=0, column=0)

    hostentry = Entry(dataframe, font=('Century Gothic', 20), show='*', bd=3)
    hostentry.grid(row=0, column=1)

    userlabel = Label(dataframe, text='          Username :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    userlabel.grid(row=1, column=0)

    userentry = Entry(dataframe, font=('Century Gothic', 20), show='*', bd=3)
    userentry.grid(row=1, column=1)

    passlabel = Label(dataframe, text='          Password :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    passlabel.grid(row=2, column=0)

    passentry = Entry(dataframe, font=('Century Gothic', 20), show='*', bd=3)
    passentry.grid(row=2, column=1)

    dblabel = Label(dataframe, text='Database Name :', font=('Times New Roman', 20), pady=10, bg='#c0f0b9')
    dblabel.grid(row=3, column=0)

    dbentry = Entry(dataframe, font=('Century Gothic', 20), show='*', bd=3)
    dbentry.grid(row=3, column=1, padx=15)

    connbutton = Button(database, text='Connect Database', font=('Times New Roman', 12), bd=3, command=destroy)
    connbutton.pack(side=BOTTOM, pady=16)

    database.mainloop()
def add():
    addwin = Toplevel()
    addwin.resizable(False, False)
    addwin.geometry('900x580')
    addwin.title("Add Student")
    addwin.config(bg='#c0f0b9')
    addframe = Frame(addwin, bg='#c0f0b9')
    addframe.place(x=0, y=20)

    def ADD():
        if len(Mobile_Numberentry.get()) == 10 and len(Addressentry.get()) != 0 and len(nameentry.get()) != 0 and len(Classentry.get()) != 0 and len(Admission_Numberentry.get()) != 0 and len(Date_of_birthentry.get()) != 0 and type(Admission_Numberentry.get() == int and type(Mobile_Numberentry.get() == int) and len(Genderentry.get()) == 1 and len(BloodGroupentry.get()) != 0 and len(Ageentry.get()) != 0 and type(Ageentry.get()) == int) and 2 <= int(Ageentry.get()) <= 19 and Genderentry.get().upper() in ('M', 'F') and BloodGroupentry.get().upper() in ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'):
            try:
                object = sql.connect(host='localhost', user='root', password='RPm@#5959', database=db)
                cursor = object.cursor()
                data = (nameentry.get().upper(), Admission_Numberentry.get().upper(), Classentry.get().upper(),
                        Date_of_birthentry.get(), Mobile_Numberentry.get(), Addressentry.get().upper(),
                        Genderentry.get().upper(), BloodGroupentry.get().upper(), Ageentry.get())
                cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', data)
                object.commit()
                addwin.destroy()
                messagebox.showinfo(title="Success", message="Student Successfully added")
                studentable.delete(*studentable.get_children())
                cursor.execute("select * from student")
                datalist = cursor.fetchall()

                for i in datalist:
                    studentable.insert('', END, values=i)
            except:
                messagebox.showerror(title="Error", message="Admission Number cannot be repeated")
        else:
            messagebox.showerror(title="Error", message="Enter correct details.")
            addwin.destroy()

    namelabel = Label(addframe, text='                     Name :', font=('Times New Roman', 20,), padx=15, pady=10,bg='#c0f0b9')
    namelabel.grid(row=0, column=0)

    nameentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    nameentry.grid(row=0, column=1)

    Admission_Numberlabel = Label(addframe, text='Admission Number :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    Admission_Numberlabel.grid(row=1, column=0)

    Admission_Numberentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    Admission_Numberentry.grid(row=1, column=1)

    Classlabel = Label(addframe, text='                      Class :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    Classlabel.grid(row=2, column=0)

    Classentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    Classentry.grid(row=2, column=1)
    Classentry.insert(0, 'Example : 12C')

    Date_of_birthlabel = Label(addframe, text='           Date of birth :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
    Date_of_birthlabel.grid(row=3, column=0)

    Date_of_birthentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    Date_of_birthentry.grid(row=3, column=1)
    Date_of_birthentry.insert(0, 'Enter in YYYY-MM-DD format')

    Mobile_Numberlabel = Label(addframe, text='      Mobile Number :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    Mobile_Numberlabel.grid(row=4, column=0)

    Mobile_Numberentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    Mobile_Numberentry.grid(row=4, column=1)

    Addresslabel = Label(addframe, text='                  Address :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    Addresslabel.grid(row=5, column=0)

    Addressentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    Addressentry.grid(row=5, column=1)

    Genderlabel = Label(addframe, text='                   Gender :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    Genderlabel.grid(row=6, column=0)

    Genderentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    Genderentry.grid(row=6, column=1)
    Genderentry.insert(0, 'M/F/O')

    BloodGrouplabel = Label(addframe, text='          Blood Group :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    BloodGrouplabel.grid(row=7, column=0)

    BloodGroupentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    BloodGroupentry.grid(row=7, column=1)
    BloodGroupentry.insert(0, 'Example : AB+')

    Agelabel = Label(addframe, text='                        Age :', font=('Times New Roman', 20), padx=15, pady=10,bg='#c0f0b9')
    Agelabel.grid(row=8, column=0)

    Ageentry = Entry(addframe, font=('Century Gothic', 20), bd=3, width=40)
    Ageentry.grid(row=8, column=1)

    addbutton = Button(addwin, text='Add', font=('Times New Roman', 16), bd=3, command=ADD)
    addbutton.pack(side=BOTTOM, pady=10, ipadx=15)

    addwin.mainloop()
def update():
    index = studentable.focus()

    if len(index) != 0:
        content = studentable.item(index)
        updatewin = Toplevel()
        updatewin.resizable(False, False)
        updatewin.geometry('900x580')
        updatewin.title("Update Student")
        updatewin.config(bg='#c0f0b9')
        updateframe = Frame(updatewin, bg='#c0f0b9')
        updateframe.place(x=0, y=20)

        def UPDATE():

            if len(Mobile_Numberentry.get()) == 10 and len(Addressentry.get()) != 0 and len(nameentry.get()) != 0 and len(Classentry.get()) != 0 and len(Admission_Numberentry.get()) != 0 and len(Date_of_birthentry.get()) != 0 and type(Admission_Numberentry.get() == int and type(Mobile_Numberentry.get() == int) and len(Genderentry.get()) == 1 and len(BloodGroupentry.get()) != 0 and len(Ageentry.get()) != 0 and type(Ageentry.get()) == int) and 2 <= int(Ageentry.get()) <= 19 and Genderentry.get().upper() in ('M', 'F') and BloodGroupentry.get().upper() in ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'):
                object = sql.connect(host='localhost', user='root', password='RPm@#5959', database=db)
                cursor = object.cursor()
                data = (nameentry.get().upper(), Classentry.get().upper(), Date_of_birthentry.get(), Mobile_Numberentry.get(),Addressentry.get().upper(), Genderentry.get().upper(), BloodGroupentry.get().upper(), Ageentry.get(),Admission_Numberentry.get())
                cursor.execute('update student set Name=%s,Class=%s,Date_of_birth=%s,Mobile_Number=%s,Address=%s,Gender=%s,Blood_Group=%s,Age=%s where Admission_Number=%s',data)
                object.commit()
                messagebox.showinfo(title='Succes', message="Student successfully updated.")
                index = ''
                updatewin.destroy()
                studentable.delete(*studentable.get_children())
                cursor.execute("select * from student")
                datalist = cursor.fetchall()

                for i in datalist:
                    studentable.insert('', END, values=i)
            else:
                messagebox.showerror(title="Error", message="Enter correct details.")
                updatewin.destroy()

        namelabel = Label(updateframe, text='                     Name :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
        namelabel.grid(row=0, column=0)

        nameentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        nameentry.insert(0, content["values"][0])
        nameentry.grid(row=0, column=1)

        Admission_Numberlabel = Label(updateframe, text='Admission Number :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
        Admission_Numberlabel.grid(row=1, column=0)

        Admission_Numberentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        Admission_Numberentry.insert(0, content["values"][1])
        Admission_Numberentry.config(state=DISABLED)
        Admission_Numberentry.grid(row=1, column=1)

        Classlabel = Label(updateframe, text='                       Class :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
        Classlabel.grid(row=2, column=0)

        Classentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        Classentry.insert(0, content["values"][2])
        Classentry.grid(row=2, column=1)

        Date_of_birthlabel = Label(updateframe, text='           Date of birth :', font=('Times New Roman', 20),padx=15, pady=10, bg='#c0f0b9')
        Date_of_birthlabel.grid(row=3, column=0)

        Date_of_birthentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        Date_of_birthentry.insert(0, content["values"][3])
        Date_of_birthentry.grid(row=3, column=1)

        Mobile_Numberlabel = Label(updateframe, text='      Mobile Number :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
        Mobile_Numberlabel.grid(row=4, column=0)

        Mobile_Numberentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        Mobile_Numberentry.insert(0, content["values"][4])
        Mobile_Numberentry.grid(row=4, column=1)

        Addresslabel = Label(updateframe, text='                  Address :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
        Addresslabel.grid(row=5, column=0)

        Addressentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        Addressentry.insert(0, content["values"][5])
        Addressentry.grid(row=5, column=1)

        Genderlabel = Label(updateframe, text='                   Gender :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
        Genderlabel.grid(row=6, column=0)

        Genderentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        Genderentry.insert(0, content["values"][6])
        Genderentry.grid(row=6, column=1)

        BloodGrouplabel = Label(updateframe, text='          Blood Group :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
        BloodGrouplabel.grid(row=7, column=0)

        BloodGroupentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        BloodGroupentry.insert(0, content["values"][7])
        BloodGroupentry.grid(row=7, column=1)

        Agelabel = Label(updateframe, text='                        Age :', font=('Times New Roman', 20), padx=15,pady=10, bg='#c0f0b9')
        Agelabel.grid(row=8, column=0)

        Ageentry = Entry(updateframe, font=('Century Gothic', 20), bd=3, width=40)
        Ageentry.insert(0, content["values"][8])
        Ageentry.grid(row=8, column=1)

        updatebutton = Button(updatewin, text='Update', font=('Times New Roman', 16), bd=3, command=UPDATE)
        updatebutton.pack(side=BOTTOM, pady=10, ipadx=15)

        updatewin.mainloop()
    else:
        messagebox.showerror(title="Error", message="Please select a record.")
def delete():
    Index = studentable.focus()

    if len(Index) != 0:
        content = studentable.item(Index)
        object = sql.connect(host='localhost', user='root', password='RPm@#5959', database=db)
        cursor = object.cursor()
        yn = messagebox.askyesno(title='Confirm Deletion', message=('Are you sure you want to delete ' + str(content['values'][0]) + ' (' + str(content['values'][1]) + ') ?'))

        if yn == True:
            cursor.execute('delete from student where Admission_Number=%s', (content['values'][1],))
            object.commit()
            studentable.delete(studentable.selection()[0])

    else:
        messagebox.showerror(title="Error", message="Please select a record.")
def search():
    searchwin = Toplevel()
    searchwin.resizable(False, False)
    searchwin.config(bg='#cbedf2')
    searchwin.geometry('420x120')
    searchframe = Frame(searchwin, bg='#cbedf2')
    searchframe.place(x=0, y=20)

    def SEARCH():
        object = sql.connect(host='localhost', user='root', password='RPm@#5959', database=db)
        cursor = object.cursor()
        try:
            cursor.execute('select * from student where Admission_Number=%s', (int(admissionentry.get()),))
        except:
            messagebox.showwarning(title='Error', message='Student not found!')
            return ()
            searchwin.destroy()
        studentable.delete(*studentable.get_children())
        data = cursor.fetchall()
        studentable.insert('', END, values=data[0])

    admissionlabel = Label(searchframe, text='Admission Number :', font=('Times New Roman', 15,), padx=15, pady=10,bg='#cbedf2')
    admissionlabel.grid(row=0, column=0)

    admissionentry = Entry(searchframe, font=('Times New Roman', 15), bd=3)
    admissionentry.grid(row=0, column=1)

    addbutton = Button(searchwin, text='Search', font=('Times New Roman', 12), bd=3, command=SEARCH)
    addbutton.pack(side=BOTTOM, pady=16)
def show():
    object = sql.connect(host='localhost', user='root', password='RPm@#5959', database=db)
    cursor = object.cursor()
    studentable.delete(*studentable.get_children())

    if showstudents['text'] == 'Show Students':
        showstudents.config(padx=25)
        cursor.execute("select * from student")
        datalist = cursor.fetchall()
        for i in datalist:
            studentable.insert('', END, values=i)
        showstudents['text'] = 'Hide Students'
    else:
        studentable.delete(*studentable.get_children())
        showstudents.config(padx=20)
        showstudents['text'] = 'Show Students'
def exit():
    yn = messagebox.askyesno(title='Exit', message='Are you sure you want to exit?')

    if yn == True:
        win.destroy()

connectbutton = Button(win, text='Connect Database', font=('Times New Roman', 10), bd=3, command=connect)
connectbutton.place(x=1060, y=35)

img = PhotoImage(file='student (1).png')
mainphoto = Label(win, image=img)
mainphoto.place(x=50, y=20)

mainlabel = Label(win, text='STUDENT MANAGEMENT SYSTEM', font=('times new roman', 40), fg='royalblue', pady=20,bg='#cbedf2')
mainlabel.pack(side=TOP)

addstudent = Button(win, text='Add Student', font=('Times New Roman', 20), bg='#dacbf2', padx=30, command=add,state=DISABLED)
addstudent.place(x=30, y=120)

updatestudent = Button(win, text='Update Student', font=('Times New Roman', 20), bg='#dacbf2', padx=15, state=DISABLED,command=update)
updatestudent.place(x=30, y=220)

deletestudent = Button(win, text='Delete Student', font=('Times New Roman', 20), bg='#dacbf2', padx=20, state=DISABLED,command=delete)
deletestudent.place(x=30, y=320)

searchstudent = Button(win, text='Search Student', font=('Times New Roman', 20), bg='#dacbf2', padx=20, state=DISABLED,command=search)
searchstudent.place(x=30, y=420)

showstudents = Button(win, text='Hide Students', font=('Times New Roman', 20), bg='#dacbf2', padx=25, state=DISABLED,command=show)
showstudents.place(x=30, y=520)

exit = Button(win, text='Exit', font=('Times New Roman', 20), bg='#dacbf2', padx=80, state=DISABLED, command=exit)
exit.place(x=30, y=620)

tree = Frame(win)
tree.place(x=280, y=100, height=590, width=910)

scrollx = Scrollbar(tree, orient=HORIZONTAL, width=25)
scrollx.pack(side=BOTTOM, fill=X)
scrolly = Scrollbar(tree, orient=VERTICAL, width=25)
scrolly.pack(side=RIGHT, fill=Y)

studentable = ttk.Treeview(tree, columns=('Name', 'Admission Number', 'Class', 'Date of birth', 'Mobile Number', 'Address', 'Gender', 'Blood Group', 'Age'), xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
studentable.pack(fill=BOTH, expand=True)
ttk.Style().configure('Treeview', rowheight=30, font=('Century Gothic', 15, 'bold'), background='#dbd9af')
scrollx.config(command=studentable.xview)
scrolly.config(command=studentable.yview)

studentable.heading('Name', text='Name')
studentable.heading('Admission Number', text='Admission Number')
studentable.heading('Class', text='Class')
studentable.heading('Date of birth', text='Date of birth')
studentable.heading('Mobile Number', text='Mobile Number')
studentable.heading('Address', text='Address')
studentable.heading('Gender', text='Gender')
studentable.heading('Blood Group', text='Blood Group')
studentable.heading('Age', text='Age')

studentable.config(show='headings')

studentable.column('Name', anchor=CENTER)
studentable.column('Admission Number', anchor=CENTER, width=170)
studentable.column('Class', anchor=CENTER, width=90)
studentable.column('Date of birth', anchor=CENTER, width=130)
studentable.column('Mobile Number', anchor=CENTER, width=150)
studentable.column('Address', anchor=CENTER, width=500)
studentable.column('Gender', anchor=CENTER, width=70)
studentable.column('Blood Group', anchor=CENTER, width=90)
studentable.column('Age', anchor=CENTER, width=40)

win.mainloop()
