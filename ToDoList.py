import tkinter as tk
from tkinter import filedialog, Text, messagebox
import pickle
import os

root = tk.Tk()

root.title("To Do App by Mankarn Sandhu")

def add_task():
    task = entrytask.get()
    if task != "":
        listboxtasks.insert(tk.END, task)
        entrytask.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning!", message="You must enter a task.")
def delete_task():
    try:
        tasksinlist = listboxtasks.curselection()[0]
        listboxtasks.delete(tasksinlist)
    except:
        tk.messagebox.showwarning(title="Warning!", message="You must select a task to delete.")

def open_list():
    tasklist = pickle.load(open("tasks.dat", "rb"))
    for task in tasklist:
        listboxtasks.insert(tk.END, task)  

def save_list():
    tasklist = listboxtasks.get(0, listboxtasks.size())
    pickle.dump(tasklist, open("tasks.dat", "wb"))



labelframe = tk.Label(root, text="To Do List", font=("Helvetica",32))
labelframe.pack(fill="both", expand = "yes")
                   
canvas = tk.Canvas(root, height = 500, width = 500, bg ="white")
canvas.pack()

frame = tk.Frame(root, bg="#77C8D2")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

listboxtasks = tk.Listbox(frame, height=18, width = 58)
listboxtasks.place(relx = 0.07, rely=0.30)

entrytask = tk.Entry(frame, width = 50)
entrytask.pack()

#Scrollbar for task listbox

scrollbar = tk.Scrollbar(frame)
scrollbar.place(rely=0.3)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


listboxtasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listboxtasks.yview)



#Buttons for different functions
addtaskbutton = tk.Button(frame, text="Add Task", width = 49, command=add_task)
addtaskbutton.place(relx = 0.07, rely = 0.05)

deletetaskbutton = tk.Button(frame, text = "Delete Task", width = 49, command= delete_task)
deletetaskbutton.place(relx=0.07, rely =0.11)

savelistbutton = tk.Button(frame, text="Save List", width = 49, command=save_list)
savelistbutton.place(relx = 0.07, rely = 0.17)

openlistbutton = tk.Button(frame, text="Open List", width = 49, command=open_list)
openlistbutton.place(relx = 0.07, rely = 0.23) 

root.mainloop()
