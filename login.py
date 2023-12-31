from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
def login():

    username = loginentry1.get()
    password = loginentry2.get()

    if username == 'admin' and password == 'admin':

        messagebox.showinfo(title='Success', message="Welcome!")
        login_win.destroy()
        import main

    else:

        messagebox.showerror(title='Error', message='Please enter correct login credentials.')
        loginentry1.delete(0, END)
        loginentry2.delete(0, END)


login_win = Tk()
login_win.title('Login')
login_win.geometry('1200x700')
login_win.resizable(False, False)
logo = PhotoImage(file='applogo.png')
login_win.iconphoto(True, logo)

bgimg = ImageTk.PhotoImage(file='bg.jpg')
loginimg = ImageTk.PhotoImage(file='logo.png')

bglabel = Label(login_win, image=bgimg)
bglabel.place(x=0, y=0)

loginframe = Frame(login_win, bg='white')
loginframe.place(x=340, y=300)

loginlabel = Label(login_win, image=loginimg, bg='white')
loginlabel.place(x=350, y=150)

logintext = Label(login_win, text='School Management System', bg='white', font=('Times New Roman', 20, 'bold'))
logintext.place(x=490, y=225)

logintext1 = Label(loginframe, text='Username:', font=('Times New Roman', 20,), bg='white')
logintext1.grid(row=1, column=0, padx=20, pady=20)

logintext2 = Label(loginframe, text='Password:', font=('Times New Roman', 20,), bg='white')
logintext2.grid(row=2, column=0, padx=20, pady=20)

loginentry1 = Entry(loginframe, font=('Century Gothic', 20), fg='royalblue', bd=3, relief=SUNKEN)
loginentry1.grid(row=1, column=1)

loginentry2 = Entry(loginframe, font=('Century Gothic', 20), fg='royalblue', bd=3, relief=SUNKEN, show='*')
loginentry2.grid(row=2, column=1)

loginbutton = Button(login_win, text='Login', font=('Times New Roman', 15), bg='cornflowerblue', cursor='hand2',padx=30, activebackground='royalblue', command=login)
loginbutton.place(x=550, y=460)

login_win.mainloop()
