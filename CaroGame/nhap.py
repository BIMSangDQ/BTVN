from ast import Pass
from concurrent.futures import thread
from tkinter import *
from tkinter import messagebox
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

positionX = []
positionO = []
cell=[]

def btn_click(event):
    if count.get()==1:
        threading.Thread(target=startcountdown,name="1").start()

    position = GetPositionWidget(event.widget.grid_info())
    global positionX
    global positionO

    if event.widget['text'] == '':
        if count.get()%2==0:
            event.widget['text']='O'
            event.widget['font'] = ('Arial',8,'bold')
            event.widget['fg']='red'
            positionO.append(position)
            Xturn.set('')
            Oturn.set('Đến lượt')
        else:
            event.widget['text']='X'
            event.widget['font'] = ('Arial',8,'bold')
            event.widget['fg']='blue'
            positionX.append(position)
            Oturn.set('')
            Xturn.set('Đến lượt')
        count.set(count.get()+1)
        countdown.set(30)

        if len(positionO)>0:
            if checkWin(positionO):
                SetScore('O')
        if len(positionX)>0:       
            if checkWin(positionX):
                SetScore('X')

def SetScore(team):
    MsgBox = messagebox.askquestion ('CaroGame',f'Team {team} thắng!\n Các bạn có muốn tiếp tục ván mới không?')
    if team == 'O':
        countOwin.set(countOwin.get()+1)
    else:
        countXwin.set(countXwin.get()+1)

    if MsgBox == 'yes':
        NewGame()      
    else:
        root.destroy()

def NewGame():
    global cell
    global positionX
    global positionO
    for btn in cell:
        btn['text'] = ''
    positionX = []
    positionO = []
    countdown.set(30)

def GetPositionWidget(grid_info):
    infos = str(grid_info).split(', ')
    column = 0
    row = 0
    for info in infos:
        if info.count("'column': ")>0:
            column = int(info.replace("'column':" , ""))
        elif info.count("'row': ")>0:
            row = int(info.replace("'row':" , ""))
    position=[column,row]
    return position

def checkWin(arr):
    #Check hàng ngang
    for i in range(0,len(arr),1):
        pos = arr[i]
        result = True
        for j in range(1,5,1):
            if findPosition(arr,[pos[0]+j,pos[1]]) == False:
                result = False
                break
        if result:
            return True

    #Check hàng dọc
    for i in range(0,len(arr),1):
        pos = arr[i]
        result = True
        for j in range(1,5,1):
            if findPosition(arr,[pos[0],pos[1]+j]) == False:
                result = False
                break
        if result:
            return True

    #Check xiên 1
    for i in range(0,len(arr),1):
        pos = arr[i]
        result = True
        for j in range(1,5,1):
            if findPosition(arr,[pos[0]+j,pos[1]+j]) == False:
                result = False
                break
        if result:
            return True

    #Check xiên 2
    for i in range(0,len(arr),1):
        pos = arr[i]
        result = True
        for j in range(1,5,1):
            if findPosition(arr,[pos[0]+j,pos[1]-j]) == False:
                result = False
                break
        if result:
            return True
    return False

def findPosition(arrp,pt):
    """
    arrp: array vị trí các quân cờ
    pt: vị trí cần tìm

    return: True nếu tìm thấy và False nếu không tìm thấy
    """
    for p in arrp:
        if p[0] == pt[0] and p[1] == pt[1]:
            return True
    return False

def startcountdown():
    countdown.set(30)
    while True:
        for i in range(0,30,1):
            try:
                countdown.set(countdown.get()-1)
                time.sleep(1)
            except:
                print("End thread")
                return
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

z=0
for i in range(0,20,1):
    for j in range(1,21,1):
        btncell = Button(frame_banco,bg='white',width=2)
        btncell.grid(row=i,column=j,sticky=NSEW)
        btncell.bind('<Button-1>',btn_click)
        cell.append(btncell)
        z+=1

loadX = Image.open('CaroGame\images\X.jpg')
resized_imageX= loadX.resize((100,100))
photo_X = ImageTk.PhotoImage(resized_imageX)
canvasX = Canvas(frame_banco, width = 100,bg='white',highlightbackground = 'white')      
canvasX.grid(row=2,rowspan=19,column=21,sticky=NSEW)
canvasX.create_image(10,10, anchor=NW, image=photo_X)

lb_Oturn = Label(frame_banco,bg="white",fg="Green",textvariable=Oturn,font=('Arial',14))
lb_Oturn.grid(row=0,rowspan=2,column=21,sticky=NSEW)

root.mainloop()