from ast import Pass
from concurrent.futures import thread
from tkinter import *
from PIL import ImageTk,Image  
import time
import threading

root = Tk()
root.title('Caro')
root.geometry('750x660')
root.resizable(False, False)

count = IntVar()
count.set(1)

countXwin = IntVar()
countXwin.set(0)

countOwin = IntVar()
countOwin.set(0) 

countdown = IntVar()
countdown.set(30)

Xturn = StringVar()
Xturn.set('Đến lượt')

Oturn = StringVar()
Oturn.set('Đến lượt')

def btn_enter(event):
    event.widget['bg']= 'lightblue'
    
def btn_leave(event):
    event.widget['bg']='white'

def btn_click(event):
    if count.get()==1:
        threading.Thread(target=restart,name="1").start()

    if event.widget['text'] == '':
        if count.get()%2==0:
            event.widget['text']='O'
            event.widget['font'] = ('Arial',8,'bold')
            event.widget['fg']='red'
            Xturn.set('')
            Oturn.set('Đến lượt')
        else:
            event.widget['text']='X'
            event.widget['font'] = ('Arial',8,'bold')
            event.widget['fg']='blue'
            Oturn.set('')
            Xturn.set('Đến lượt')
        count.set(count.get()+1)
        countdown.set(30)

def setX():
    Pass

def setY():
    Pass

def checkWin():
    Pass

def restart():
    countdown.set(30)
    while True:
        for i in range(0,30,1):
            countdown.set(countdown.get()-1)
            time.sleep(1)
        count.set(count.get()+1)
        if count.get()%2==0:
            Xturn.set('')
            Oturn.set('Đến lượt')
        else:
            Oturn.set('')
            Xturn.set('Đến lượt')
        countdown.set(30)


##
frameInfo = LabelFrame( root, relief = FLAT,bg='white', bd=10)
frameInfo.grid(row=0,column=0,columnspan=3,padx=15,pady=(15,0),sticky=NSEW)
frameInfo.columnconfigure(0,minsize = 200)
frameInfo.columnconfigure(1,minsize = 300)
frameInfo.columnconfigure(2,minsize=200)

lb_d1 = Label(frameInfo,bg="white",text='Điểm',font=('Arial',14,'underline'))
lb_d1.grid(row=0,column=0,sticky=NSEW)

lb_time = Label(frameInfo,bg="white",text='Thời gian',font=('Arial',14))
lb_time.grid(row=0,column=1,sticky=NSEW)

lb_d2 = Label(frameInfo,bg="white",text='Điểm',font=('Arial',14,'underline'))
lb_d2.grid(row=0,column=2,sticky=NSEW)

lb_d1show = Label(frameInfo,bg="white",fg="blue",textvariable=countOwin,font=('Arial',12))
lb_d1show.grid(row=1,column=0,sticky=NSEW)

lb_timecount = Label(frameInfo,bg="white",textvariable=countdown,font=('Arial',14))
lb_timecount.grid(row=1,column=1,sticky=NSEW)

lb_d2show = Label(frameInfo,bg="white",fg="blue",textvariable=countXwin,font=('Arial',12))
lb_d2show.grid(row=1,column=2,sticky=NSEW)

##
frame_banco = LabelFrame( root, relief = FLAT,bg='white', bd=10)
frame_banco.grid(row=1,column=0,columnspan=3,padx=15,pady=15,sticky=NSEW)
frame_banco.columnconfigure(0,minsize = 100)
frame_banco.columnconfigure(21,minsize=100)
frame_banco.rowconfigure(21,minsize=0)

lb_Xturn = Label(frame_banco,bg="white",fg="Green",textvariable=Xturn,font=('Arial',14))
lb_Xturn.grid(row=0,rowspan=2,column=0,sticky=NSEW)

loadO = Image.open('CaroGame\images\O.jpg')
resized_imageO= loadO.resize((100,100))
photo_O = ImageTk.PhotoImage(resized_imageO)
canvasO = Canvas(frame_banco, width = 100,bg='white',highlightbackground = 'white')      
canvasO.grid(row=2,rowspan=19,column=0,sticky=NSEW)
canvasO.create_image(10,10, anchor=NW, image=photo_O)

for i in range(0,20,1):
    for j in range(1,21,1):
        cell = Button(frame_banco,bg='white',width=2)#,command=lambda:threading.Thread(target=restart,name=count.get()).start())
        cell.grid(row=i,column=j,sticky=NSEW)
        cell.bind('<Button-1>',btn_click)
        cell.bind('<Enter>', btn_enter)
        cell.bind('<Leave>', btn_leave)

loadX = Image.open('CaroGame\images\X.jpg')
resized_imageX= loadX.resize((100,100))
photo_X = ImageTk.PhotoImage(resized_imageX)
canvasX = Canvas(frame_banco, width = 100,bg='white',highlightbackground = 'white')      
canvasX.grid(row=2,rowspan=19,column=21,sticky=NSEW)
canvasX.create_image(10,10, anchor=NW, image=photo_X)

lb_Oturn = Label(frame_banco,bg="white",fg="Green",textvariable=Oturn,font=('Arial',14))
lb_Oturn.grid(row=0,rowspan=2,column=21,sticky=NSEW)



root.mainloop()