import tkinter
import random

root = tkinter.Tk()

title = tkinter.Label(root,text="TO-DO List", bg='white')
title.pack()
displa = tkinter.Label(root,text='',bg='white')
displa.pack()

task_entry = tkinter.Entry(root,text="",width = 15)
task_entry.pack()

tasks = []

def show_tasks():
    tasklist.delete(0, tkinter.END)
    for task in tasks:
        tasklist.insert(tkinter.END, task)

# Add a new task
def addtask():
    task = task_entry.get()
    if task:
        tasks.append(task)
        show_tasks()
        task_entry.delete(0, tkinter.END)

# Delete selected task
def dele():
    selected = tasklist.curselection()
    if selected:
        tasks.pop(selected[0])
        show_tasks()

# Delete all tasks
def delall():
    tasks.clear()
    show_tasks()

# Sort tasks A-Z
def asc():
    tasks.sort()
    show_tasks()

# Sort tasks Z-A
def dsc():
    tasks.sort(reverse=True)
    show_tasks()

# Exit the app
def ex():
    root.destroy()



addtask = tkinter.Button(text='Add Task',fg='white',bg='black',command=addtask)
addtask.pack()
dele = tkinter.Button(text='Delete',fg='white',bg='black',command=dele)
dele.pack()
delall = tkinter.Button(text='Delete all',fg='white',bg='black',command=delall)
delall.pack()
asc = tkinter.Button(text='Sort ASC',fg='white',bg='black',command=asc)
asc.pack()
dsc = tkinter.Button(text='Sort DSC',fg='white',bg='black',command=dsc)
dsc.pack()
ex=tkinter.Button(text='Exit',fg='white',bg='black', command=ex)
ex.pack()

tasklist = tkinter.Listbox(root, width=40, height=10)
tasklist.pack()

root.mainloop()
