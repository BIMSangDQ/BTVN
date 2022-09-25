from tkinter import *
from tkinter import ttk
from tkinter import messagebox

bunbo_price=50000
pho_price=40000
comtam_price=35000

def tinhtien():
    tamtinh = 0
    tamtinh += bunbo_var.get()*int(bunbo_sl.get())
    tamtinh += pho_var.get()*int(pho_sl.get())
    tamtinh += comtam_var.get()*int(comtam_sl.get())
    sotien = tamtinh*httt.get()/100
    return sotien

def format_sotien(sotien):
    count = 0
    sotien_format = ''
    for i in range(len(str(sotien))-1,-1,-1):
        if count == 3:
            sotien_format = str(sotien)[i]+'.' + sotien_format
            count = 0
        else:
            sotien_format = str(sotien)[i] + sotien_format
        count +=1
    return sotien_format

def showtext():
    sotien = tinhtien()
    if sotien == 0:
        paytext.set('Thanh toán')
    else:
        paytext.set(f"Thanh toán {format_sotien(int(sotien))} VNĐ")

def chose_bunbo():
    if (bunbo_var.get() == bunbo_price):
        bunbo_sl.set("1")
    else:
        bunbo_sl.set('0')
    showtext()

def set_slbunbo(event):
    if int(bunbo_sl.get())>0:
        bunbo_var.set(bunbo_price)
    else:
        bunbo_var.set(0)
    showtext()

def chose_pho():
    if (pho_var.get() == pho_price):
        pho_sl.set('1')
    else:
        pho_sl.set('0')
    showtext()

def set_slpho(event):
    if int(pho_sl.get())>0:
        pho_var.set(pho_price)
    else:
        pho_var.set(0)
    showtext()

def chose_comtam():
    if (comtam_var.get() == comtam_price):
        comtam_sl.set('1')
    else:
        comtam_sl.set('0')
    showtext()

def set_slcomtam(event):
    if int(comtam_sl.get())>0:
        comtam_var.set(comtam_price)
    else:
        comtam_var.set(0)
    showtext()

def showmessage(event):
    event.widget['bg']='lightgreen'
    sotien = tinhtien()
    if sotien==0:
        messagebox.showwarning("Thanh toán", "Bạn chưa chọn món!")
    else:
        messagebox.askquestion("Thanh toán", f"Bạn có muốn thanh toán số tiền là {format_sotien(int(sotien))} VNĐ")

def select_pttt():
    if httt.get() == 100:
        rd_tienmat["fg"] = 'blue'
        rd_ck["fg"] = 'black'
    else:
        rd_tienmat["fg"] = 'black'
        rd_ck["fg"] = 'blue'
    showtext()

def btn_enter(event):
    event.widget['bg']= 'green'
    
def btn_leave(event):
    event.widget['bg']='lightgreen'

root = Tk()
root.title('Menu demo')
root.geometry('500x370')
root.resizable(False, False)
root.configure(background="lightblue")
root.columnconfigure(0,weight = 3)
root.columnconfigure(1,weight = 1 )

root.rowconfigure(0,weight = 1)
root.rowconfigure(1,weight = 1)
root.rowconfigure(2,weight = 1)

slarr = [f'{i}' for i in range(0,101,1)]

bunbo_var = IntVar()
bunbo_var.set(0)
bunbo_sl = StringVar()
bunbo_sl.set('0')

pho_var = IntVar()
pho_var.set(0)
pho_sl = StringVar()
pho_sl.set('0')

comtam_var = IntVar()
comtam_var.set(0)
comtam_sl = StringVar()
comtam_sl.set('0')

httt = IntVar()
httt.set(100)

paytext = StringVar()
paytext.set('Thanh toán')

menuframe = LabelFrame( root, relief = FLAT,bg='white', bd=10)
menuframe.grid(row=0,column=0,columnspan=2,padx=15,pady=15,sticky=NSEW)
menuframe.columnconfigure(0,weight = 3)
menuframe.columnconfigure(1,weight = 1 )

menuframe.rowconfigure(0)
menuframe.rowconfigure(1)
menuframe.rowconfigure(2)
menuframe.rowconfigure(2)

lb_menu = Label(menuframe,bg="white",text='MÓN',font=('Arial',12,'underline'))
lb_menu.grid(row=0,column=0,sticky=NSEW)

lb_sl = Label(menuframe,bg="white",text='SỐ LƯỢNG',font=('Arial',12,'underline'))
lb_sl.grid(row=0,column=1,sticky=NSEW)

cb_bunbo = Checkbutton(menuframe,bg="white",text="Bún bò (50.000VNĐ)",onvalue= bunbo_price,offvalue=0, variable = bunbo_var,command=chose_bunbo)
cb_bunbo.grid(row=1,column=0,padx=10,pady=10,sticky=W)

cbb_bunbo = ttk.Combobox(menuframe,values = slarr, state = 'readonly',textvariable = bunbo_sl)
cbb_bunbo.grid(row=1,column=1,padx=50,pady=10,sticky=NSEW)
cbb_bunbo.bind("<<ComboboxSelected>>",set_slbunbo)

cb_pho = Checkbutton(menuframe,bg="white",text="Phở (40.000VNĐ)",onvalue= pho_price,offvalue=0, variable = pho_var,command=chose_pho)
cb_pho.grid(row=2,column=0,padx=10,pady=10,sticky=W)

cbb_pho = ttk.Combobox(menuframe,values = slarr, state = 'readonly',textvariable = pho_sl)
cbb_pho.grid(row=2,column=1,padx=50,pady=10,sticky=NSEW)
cbb_pho.bind("<<ComboboxSelected>>",set_slpho)

cb_comtam = Checkbutton(menuframe,bg="white",text="Cơm tấm (35.000VNĐ)",onvalue= comtam_price,offvalue=0, variable = comtam_var,command=chose_comtam)
cb_comtam.grid(row=3,column=0,padx=10,pady=10,sticky=W)

cbb_comtam = ttk.Combobox(menuframe,values = slarr, state = 'readonly',textvariable = comtam_sl)
cbb_comtam.grid(row=3,column=1,padx=50,pady=10,sticky=NSEW)
cbb_comtam.bind("<<ComboboxSelected>>",set_slcomtam)

menupay = LabelFrame( root, relief = FLAT,bg='white', bd=10,font=('Arial',12,'underline'),text='Hình thức thanh toán')
menupay.grid(row=1,column=0,columnspan=2,padx=15,pady=(0,15),sticky=NSEW)
menupay.columnconfigure(0,weight = 1)
menupay.columnconfigure(1,weight = 1 )

rd_tienmat = Radiobutton(menupay,bg="white",text="Tiền mặt",value=100,variable=httt,command=select_pttt,fg='blue')
rd_tienmat.grid(row=5,column=0,padx=10,pady=10,sticky=NSEW)

rd_ck = Radiobutton(menupay,bg="white",text="Chuyển khoản (giảm 5%)",value=95,variable=httt,command=select_pttt,fg='black')
rd_ck.grid(row=5,column=1,padx=10,pady=10,sticky=NSEW)

btn_thanhtoan = Button(root,relief=RAISED,bg="lightgreen",textvariable=paytext)
btn_thanhtoan.grid(row=2,column=0,columnspan=2,padx=15,pady=(0,15),sticky=NSEW)
btn_thanhtoan.bind("<Button-1>",showmessage)
btn_thanhtoan.bind('<Enter>', btn_enter)
btn_thanhtoan.bind('<Leave>', btn_leave)

root.mainloop()