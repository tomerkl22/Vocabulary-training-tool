from tkinter import * 
from tkinter import ttk
import sqlite3

window=Tk()

window.title("Dictionary")
label=Label(window,text="Adding Word", font=('arial',15,'bold'),bg="black",fg="white")
label.pack(side=TOP,fill=X)
label=Label(window,text="", font=('arial',15,'bold'),bg="black",fg="white")
label.pack(side=BOTTOM,fill=X)


def create():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement, name TEXT, password TEXT, sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
    conn.commit()
    conn.close()
create()

label=Label(window,text="Word", font=('arial',13,'bold'))
label.place(x=30,y=60)

name_entry=StringVar()
name_entry=ttk.Entry(window,textvariable=name_entry)
name_entry.place(x=170,y=60)
name_entry.focus()

label=Label(window,text="Meaning", font=('arial',13,'bold'))
label.place(x=30,y=100)

name_entry2=StringVar()
name_entry2=ttk.Entry(window,textvariable=name_entry2)
name_entry2.place(x=170,y=100)

def savedata():
    conn=sqlite3.connect('database.db')
    c=conn.cursor() 
    c.execute('INSERT INTO users(name,password) VALUES (?,?)',(name_entry.get(),name_entry2.get()))
    conn.commit()
    print("saved")
    
btn=ttk.Button(window,text='Save Date',command=savedata)
btn.place(x=170,y=160,width=125,height=30) 

window.geometry('400x400')
window.resizable(False,False)
window.mainloop()
