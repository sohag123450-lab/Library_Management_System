from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import PhotoImage
from tkinter import messagebox
import openpyxl
import pyxll
from openpyxl import load_workbook
import ast



def signin():
    username=user.get()
    password=passw.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()


    if username in r.keys() and password==r[username]:
        messagebox.showinfo('login','successfully done')
        root.destroy()
        import dashboard



    else:
        messagebox.showerror('Wrong','username or password wrong')

global user
global passw

root = Tk()
root.iconbitmap(r'books.ico')
root.title('Library Management System')
root.geometry('925x500+300+200')
root.configure(bg='white')
root.resizable(False, False)
img = PhotoImage(file='login.png')
label1 = Label(root, image=img, bg='white')
label1.place(x=0, y=50)
heading = Label(root, text='Sign in', fg='black', bg='white', font=('Areal', 15, 'bold', 'underline'))
heading.place(x=700, y=85)
def on_enter(e):
    user.delete(0,'end')

user = Entry(root, width=30, fg='black', bg='white', bd='5')
user.place(x=650, y=150)
user.insert(0, 'Username')
user.bind("<FocusIn>",on_enter)
def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')
user.bind("<FocusOut>",on_leave)
def on_enter(e):
    passw.delete(0,'end')

passw = Entry(root, width=30, fg='black', bg='white', bd='5')
passw.place(x=650, y=200)
passw.insert(0, 'Password')
passw.bind("<FocusIn>",on_enter)


def on_leave(e):
    if passw.get() == '':
        passw.insert(0, 'Password')
passw.bind("<FocusOut>",on_leave)
button1 = Button(root, width=25, pady=0, cursor='hand2', text='Sign in', bg='blue', fg='black', command=signin)
button1.place(x=653, y=240)

label3=Label(root,text="Don't have any account?",fg='black',bg='white')
label3.place(x=653,y=280)
def signup():
    root.destroy()
    import signup


button2=Button(root, width=5, pady=0, cursor='hand2', text='Sign Up', bg='blue', fg='black',command=signup)
button2.place(x=792, y=278)
root.mainloop()
