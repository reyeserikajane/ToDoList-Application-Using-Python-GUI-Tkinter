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
bg_img = PhotoImage(file="images/bg.png") 
set_bgimg = Label(root, image=bg_img)
set_bgimg.pack()

# Top Bar
# top_image = PhotoImage(file=)
# Add task

# Delete task



root.mainloop()