from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import PhotoImage
from tkinter import messagebox
import openpyxl
import pyxll
from openpyxl import load_workbook
import ast



def signup():
    username = user.get()
    password = passw.get()
    conform_password = cpassw.get()

    if password == conform_password:
        try:
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('datasheet.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('signup', 'Successfully signup')

        except Exception as e:
            print(e)
            file = open('datasheet.txt', 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid', 'Both password should match')



window = Tk()
window.iconbitmap(r'books.ico')
window.title('Library Management System')
window.geometry('925x500+300+200')
window.configure(bg='white')
window.resizable(False, False)
img = PhotoImage(file='login.png')
label1 = Label(window, image=img, bg='white')
label1.place(x=0, y=50)
heading = Label(window, text='Sign UP', fg='black', bg='white', font=('Areal', 15, 'bold', 'underline'))
heading.place(x=700, y=85)
def on_enter(e):
    user.delete(0,'end')

user = Entry(window, width=30, fg='black', bg='white', bd='5')
user.place(x=650, y=150)
user.insert(0, 'Username')
user.bind("<FocusIn>",on_enter)
def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')
user.bind("<FocusOut>",on_leave)
def on_enter(e):
    passw.delete(0,'end')

passw = Entry(window, width=30, fg='black', bg='white', bd='5')
passw.place(x=650, y=200)
passw.insert(0, 'Password')
passw.bind("<FocusIn>",on_enter)


def on_leave(e):
    if passw.get() == '':
        passw.insert(0, 'Password')
passw.bind("<FocusOut>",on_leave)





def on_enter(e):
    cpassw.delete(0,'end')


cpassw = Entry(window, width=30, fg='black', bg='white', bd='5')
cpassw.place(x=650, y=250)
cpassw.insert(0, 'Confirm_Password')
cpassw.bind("<FocusIn>",on_enter)

def on_leave(e):
    if cpassw.get() == '':
        cpassw.insert(0,'Confirm_password')

cpassw.bind("<FocusOut>",on_leave)



button1 = Button(window, width=25, pady=0, cursor='hand2', text='Sign Up', bg='blue', fg='black', command=signup)
button1.place(x=653, y=290)
label2=Label(window, text='I have an account.', fg='black', bg='white')
label2.place(x=650,y=330)
def signin():
    window.destroy()
    import main

button2 = Button(window, width=5, pady=0, cursor='hand2', text='Sign In', bg='blue', fg='black',command=signin)
button2.place(x=753, y=328)

window.mainloop()
