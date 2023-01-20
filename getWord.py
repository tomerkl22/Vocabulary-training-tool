from tkinter import * 
from tkinter import ttk
import sqlite3
import random

window=Tk()
window.iconbitmap('c:/guis/TomerCon.ico')

window.title("psy")
label=Label(window,text="Find the meaning", font=('arial',15,'bold'),bg="black",fg="white")
label.pack(side=TOP,fill=X)
label2=Label(window,text="", font=('arial',15,'bold'),bg="black",fg="white")
label2.pack(side=BOTTOM,fill=X)



def getword():
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM users;")
        results= cursor.fetchall()
        length=len(results)
        global label
        label.destroy()
        global x
        x=random.randint(0,length-1)
        label=Label(window,text=results[x], font=('arial',15,'bold'))
        label.place(x=170,y=100)
        cursor.close()
        connection.close()

def meaning():
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM users;")
        results= cursor.fetchall()
        global label2
        label2.destroy()
        label2=Label(window, text=results[x], font=('arial',15,'bold'))
        label2.place(x=170,y=150)
        cursor.close()
        connection.close()
        
	
btn=ttk.Button(window,text='Get a word',command=getword) #get a word 
btn.place(x=170,y=250,width=125,height=30)
btn1=ttk.Button(window, text='Meaning', command=meaning)
btn1.place(x=170,y=300, width=125,height=30)

window.geometry('400x400')
window.resizable(False,False)
window.mainloop()
