# Programmed by Erika Jane T. Reyes
# To Do List Application Using Python GUI Tkinter

import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list = []
def addTask():
    task = todo_entry.get()
    todo_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\{task}")
        task_list.append(task)
        todolist_container.insert(END, task)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

            for task in tasks:
                if task != "\n":
                    task_list.append(task)
                    todolist_container.insert(END, task)
    except:
        file = open("tasklist.txt","r")
        file.close()

# Application Icon
image_icon = PhotoImage(file="images/todolisticon.png")
root.iconphoto(False,image_icon)

# Window Background
bg_img = root.configure(background="#F9E7E5")

# Top Bar
top_img = PhotoImage(file="images/topbar.png")
set_topimg = Label(root, image=top_img).place(x=20,y=10)

heading = Label(root, text="MY TO-DO LIST", font="arial 18 bold", fg="black", bg="#C7A15B")
heading.place(x=115,y=35)

# Add task
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

todo = StringVar()
todo_entry = Entry(frame, width=18, font="arial 20", bd=0)
todo_entry.place(x=10, y=7)
todo_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#FF86C3", fg="black", bd=0, command=addTask)
button.place(x=300,y=0)

# To Do List Container
frame1 = Frame(root, bd=1, width=700, height=280,bg="#A82D6B")
frame1.pack(pady=(240,0))

todolist_container = Listbox(frame1, font=('arial',12), width=40,height=16,bg="#A82D6B",fg="pink", cursor="hand2", selectbackground="black")
todolist_container.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

todolist_container.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todolist_container.yview)

openTaskFile()

# Delete task
delete_icon = PhotoImage(file="images/delete.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=20)


root.mainloop()