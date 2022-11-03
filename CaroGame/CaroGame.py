import threading
import time
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

root = Tk()
root.title('Caro')
root.geometry('750x780')
root.resizable(False, False)
root.configure(bg='blue')

#region variable
countXwin = IntVar()
countXwin.set(0)

countOwin = IntVar()
countOwin.set(0) 

countdown = IntVar()

Oturn = StringVar()
Oturn.set('')

Xturn = StringVar()
Xturn.set('Đến lượt')

timeSetting = IntVar()

winSetting = IntVar()

newgame= False

positionX = []
positionO = []
cell=[]
path = 'CaroGame\Setting.txt'
#endregion 

#region method
def btn_enter(event):
    event.widget['bg']= 'skyblue'

def btn_leave(event):
    event.widget['bg']='white'

def btn_savesetting(event):
    global path
    try:
        f = open(path,"w",encoding="utf8")
        f.write(f'{timeSetting.get()}|{winSetting.get()}')
    except:
        messagebox.ERROR ('CaroGame',f'Lỗi nhập liệu vui lòng kiểm tra lại')
    load_setting()
    
def load_setting():
    global path
    f = open(path,"r",encoding="utf8")
    for line in f:
        items = line.split('|')
        timeSetting.set(items[0])
        winSetting.set(items[1])
    countdown.set(timeSetting.get())

def btn_click(event):
    global newgame
    if newgame==False:
        newgame = True
        threading.Thread(target=startcountdown).start()

    position = GetPositionWidget(event.widget.grid_info())

    global positionX
    global positionO

    if event.widget['text'] == '':
        if Oturn.get() == 'Đến lượt':
            event.widget['text']='O'
            event.widget['font'] = ('Arial',8,'bold')
            event.widget['fg']='red'
            positionO.append(position)
            Oturn.set('')
            Xturn.set('Đến lượt')
        else:
            event.widget['text']='X'
            event.widget['font'] = ('Arial',8,'bold')
            event.widget['fg']='blue'
            positionX.append(position)
            Xturn.set('')
            Oturn.set('Đến lượt')
        countdown.set(timeSetting.get())
        setbackgound()

def SetScore(team):
    MsgBox = messagebox.askquestion ('CaroGame',f'Team {team} thắng!\n Các bạn có muốn tiếp tục ván mới không?')
    if team == 'O':
        countOwin.set(countOwin.get()+1)
    else:
        countXwin.set(countXwin.get()+1)
    setbackgound()

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
        btn['bg'] = 'white'
    positionX = []
    positionO = []
    countdown.set(timeSetting.get())

def GetPositionWidget(grid_info):
    #infos = str(grid_info).split(', ')
    column = grid_info["column"]
    row = grid_info["row"]
    position=[column,row]
    return position

def check():
    global newgame
    global Oturn
    global Xturn
    global positionO
    global positionX
    if len(positionO)>0:
        if subcheck(positionO):
            Oturn.set('')
            Xturn.set('Đến lượt')
            newgame = False
            SetScore('O')
    if len(positionX)>0:       
        if subcheck(positionX):
            Oturn.set('Đến lượt')
            Xturn.set('')
            newgame = False
            SetScore('X')

def subcheck(arr):
    #Check hàng ngang
    for i in range(0,len(arr),1):
        pos = arr[i]
        result = True
        for j in range(1,winSetting.get(),1):
            if findPosition(arr,[pos[0]+j,pos[1]]) == False:
                result = False
                break
        if result:
            position = []
            for j in range(0,winSetting.get(),1):
                position.append([pos[0]+j,pos[1]])
                highlight(position)
            return True

    #Check hàng dọc
    for i in range(0,len(arr),1):
        pos = arr[i]
        result = True
        for j in range(1,winSetting.get(),1):
            if findPosition(arr,[pos[0],pos[1]+j]) == False:
                result = False
                break
        if result:
            position = []
            for j in range(0,winSetting.get(),1):
                position.append([pos[0],pos[1]+j])
                highlight(position)
            return True

    #Check xiên 1
    for i in range(0,len(arr),1):
        pos = arr[i]
        result = True
        for j in range(1,winSetting.get(),1):
            if findPosition(arr,[pos[0]+j,pos[1]+j]) == False:
                result = False
                break
        if result:
            position = []
            for j in range(0,winSetting.get(),1):
                position.append([pos[0]+j,pos[1]+j])
                highlight(position)
            return True

    #Check xiên 2
    for i in range(0,len(arr),1):
        pos = arr[i]
        result = True
        for j in range(1,winSetting.get(),1):
            if findPosition(arr,[pos[0]+j,pos[1]-j]) == False:
                result = False
                break
        if result:
            position = []
            for j in range(0,winSetting.get(),1):
                position.append([pos[0]+j,pos[1]-j])
                highlight(position)
            return True
    return False

def highlight(posar):
        for position in posar:
            for btn in cell:
                p = GetPositionWidget(btn.grid_info())
                if p[0] == position[0] and p[1] == position[1]:
                    btn['bg'] = 'lightGreen'

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
    global newgame 
    countdown.set(timeSetting.get())
    while newgame:
        for i in range(0,timeSetting.get(),1):
            try:
                countdown.set(countdown.get()-1)
                time.sleep(1)
                if newgame == False or countdown.get()==0:
                    break
            except:
                print("End thread")
                return
        
        if countdown.get()==0:
            if Xturn.get() == 'Đến lượt':
                Xturn.set('')
                Oturn.set('Đến lượt')
            else:
                Oturn.set('')
                Xturn.set('Đến lượt')
            countdown.set(timeSetting.get())
            setbackgound()

def setbackgound():
    if Xturn.get() == 'Đến lượt':
        root['bg']='blue'
    else:
        root['bg'] = 'red'
#endregion

#region Thời gian, tính điểm
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
#endregion

#region bàn cờ
frame_banco = LabelFrame( root, relief = FLAT,bg='white', bd=10)
frame_banco.grid(row=1,column=0,columnspan=3,padx=15,pady=15,sticky=NSEW)
frame_banco.columnconfigure(0,minsize = 100)
frame_banco.columnconfigure(21,minsize=100)
frame_banco.rowconfigure(21,minsize=0)

lb_Oturn = Label(frame_banco,bg="white",fg="Green",textvariable=Oturn,font=('Arial',14))
lb_Oturn.grid(row=6,rowspan=2,column=0,sticky=NSEW)

loadO = Image.open('CaroGame\images\O.jpg')
resized_imageO= loadO.resize((100,100))
photo_O = ImageTk.PhotoImage(resized_imageO)
canvasO = Canvas(frame_banco, width = 100,bg='white',highlightbackground = 'white')      
canvasO.grid(row=8,rowspan=10,column=0,sticky=NSEW)
canvasO.create_image(10,10, anchor=NW, image=photo_O)

z=0
for i in range(0,20,1):
    for j in range(1,21,1):
        btncell = Button(frame_banco,bg='white',width=2,command=check)
        btncell.grid(row=i,column=j,sticky=NSEW)
        btncell.bind('<Button-1>',btn_click)
        cell.append(btncell)
        z+=1

loadX = Image.open('CaroGame\images\X.jpg')
resized_imageX= loadX.resize((100,100))
photo_X = ImageTk.PhotoImage(resized_imageX)
canvasX = Canvas(frame_banco, width = 100,bg='white',highlightbackground = 'white')      
canvasX.grid(row=8,rowspan=10,column=21,sticky=NSEW)
canvasX.create_image(10,10, anchor=NW, image=photo_X)

lb_Xturn = Label(frame_banco,bg="white",fg="Green",textvariable=Xturn,font=('Arial',14))
lb_Xturn.grid(row=6,rowspan=2,column=21,sticky=NSEW)
#endregion

#region setting
frame_setting = LabelFrame( root, relief = FLAT,bg='white', bd=10, text='Cài đặt',font=('Arial',12,'underline','bold'))
frame_setting.grid(row=2,column=0,columnspan=3,padx=15,pady=(0,15),sticky=NSEW)
frame_setting.columnconfigure(0,minsize = 300)
frame_setting.columnconfigure(1,minsize=100)
frame_setting.columnconfigure(2,minsize=100)
frame_setting.columnconfigure(3,minsize=50)
frame_setting.columnconfigure(4,minsize=100)

lb_t_setting = Label(frame_setting,bg="white",text='Thời gian tối đa mỗi lượt đánh (s):',font=('Arial',10),anchor=W)
lb_t_setting.grid(row=0,column=0,sticky=NSEW)

et_time_setting = Entry(frame_setting,bg="white",font=('Arial',10),textvariable=timeSetting)
et_time_setting.grid(row=0,column=2,sticky=NSEW)

et_time_setting = Entry(frame_setting,bg="white",font=('Arial',10),textvariable=timeSetting)
et_time_setting.grid(row=0,column=2,sticky=NSEW)

lb_win_setting = Label(frame_setting,bg="white",text='Thắng khi đạt đường đường thẳng dài:',font=('Arial',10),anchor=W)
lb_win_setting.grid(row=2,column=0,sticky=NSEW)

et_win_setting = Entry(frame_setting,bg="white",font=('Arial',10),textvariable=winSetting)
et_win_setting.grid(row=2,column=2,sticky=NSEW)

btn_saveSetting = Button(frame_setting,bg='white',fg='blue',text='Lưu cài đặt')
btn_saveSetting.grid(row=3,column=4,sticky=NSEW)
btn_saveSetting.bind('<Enter>',btn_enter)
btn_saveSetting.bind('<Leave>',btn_leave)
btn_saveSetting.bind('<Button-1>',btn_savesetting)
#endregion 

load_setting()

root.mainloop()