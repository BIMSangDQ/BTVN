from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image  

root = Tk()
root.geometry("300x500")

photo = Image.open('220925_game\concho.jpg')
lb_picture = Label(root,image = photo)
lb_picture.grid(column=0,row = 0)

root.mainloop()