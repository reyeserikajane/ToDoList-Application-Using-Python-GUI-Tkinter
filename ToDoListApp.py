# Programmed by Erika Jane T. Reyes
# To Do List Application Using Python GUI Tkinter

import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list = []

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

# Delete task



root.mainloop()