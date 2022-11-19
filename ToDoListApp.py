# Programmed by Erika Jane T. Reyes
# To Do List Application Using Python GUI Tkinter

import tkinter
from tkinter import *
import tkinter.messagebox
import pickle

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

def addTask():
    task = todo_entry.get()
    if task != "":
        todolist_container.insert(tkinter.END, task)
        todo_entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def deleteTask():
    try:
        task_index = todolist_container.curselection()[0]
        todolist_container.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def saveTasks():
    tasks = todolist_container.get(0, todolist_container.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
    tkinter.messagebox.showinfo(title="Saved!", message="Tasks entered are now saved.")


def loadTasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        todolist_container.delete(0, tkinter.END)
        for task in tasks:
            todolist_container.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="No tasks saved.")

# Application Icon
image_icon = PhotoImage(file="images/todolisticon.png")
root.iconphoto(False,image_icon)

# Window Background
bg_img = root.configure(background="#F9E7E5")

# Top Bar
top_img = PhotoImage(file="images/topbar.png")
set_topimg = Label(root, image=top_img).place(x=-53,y=10)
todo_img = PhotoImage(file="images/todo.png")
set_todimg = Label(root, image=todo_img).place(x=5,y=50)
me_img = PhotoImage(file="images/me.png")
set_meimg = Label(root, image=me_img).place(x=335,y=50)

# Add task 
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

todo = StringVar()
todo_entry = Entry(frame, width=18, font=("comic sans ms", 18), bd=0)
todo_entry.place(x=10, y=7)
todo_entry.focus()

add_button_fnt = ("Comic Sans MS", 20, "bold")
add_button = Button(frame, text="Add", width=6, bg="#9F516D", fg="white", bd=0, command=addTask)
add_button.place(x=300, y=-7)
add_button.configure(font=add_button_fnt)

# To Do List Container
frame1 = Frame(root, bd=1, width=700, height=280,bg="#E4A1B9")
frame1.pack(pady=(240,0))

todolist_container = Listbox(frame1, font=('Comic Sans Ms',15,"bold"), width=30,height=10,bg="#E4A1B9",fg="black", cursor="hand2", selectbackground="#9F516D")
todolist_container.pack(side=LEFT, fill=BOTH, padx=2)


scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

todolist_container.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todolist_container.yview)

# Delete task icon
delete_icon = PhotoImage(file="images/delete.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).place(x=105, y=550)
delete_text = Label(root, text="Delete", font=("Comic Sans Ms", 12), bg="#F9E7E5").place(x=105, y=605)

# Save task icon
save_icon = PhotoImage(file="images/save.png")
Button(root, image=save_icon, bd=0, command=saveTasks).place(x=180, y=550)
save_text = Label(root, text="Save", font=("Comic Sans Ms", 12), bg="#F9E7E5").place(x=187, y=605)

# Load task icon
load_icon = PhotoImage(file="images/load.png")
Button(root, image=load_icon, bd=0, command=loadTasks).place(x=255, y=550)
load_text = Label(root, text="Load", font=("Comic Sans Ms", 12), bg="#F9E7E5").place(x=263, y=605)

root.mainloop()
