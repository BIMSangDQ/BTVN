from ast import Try
from posixpath import split
from tkinter import *

highlightcolor = 'lightblue'
fontbuttonsize = 10
textfont = "Helvetica"

#window
window = Tk()
window.title("Calculator")
window.geometry("250x400")

window.columnconfigure(0,weight = 1)
window.columnconfigure(1,weight = 1)
window.columnconfigure(2,weight = 1)
window.columnconfigure(3,weight = 1)
window.columnconfigure(4,weight = 1)

window.rowconfigure(0,weight = 3)
window.rowconfigure(1,weight = 2)
window.rowconfigure(2,weight = 2)
window.rowconfigure(3,weight = 2)
window.rowconfigure(4,weight = 2)
window.rowconfigure(5,weight = 2)
window.rowconfigure(6,weight = 2)
window.configure(bg=highlightcolor)

#event
def btn_enter(event):
    event.widget['bg']= highlightcolor

def btn_leave(event):
    event.widget['bg']='SystemButtonFace'

def btn_click(event):
    if et_result['text'] == '0' or et_result['text'].count('=')==1:
        et_result['text'] =  event.widget['text']
    else:
        et_result['text'] += event.widget['text']

def btn_equalclick(event):
    result = 0
    inputtext = et_result['text']
    inputtext = inputtext.replace('-','+-')
    cals = inputtext.split('+')
    for subtext in cals:
        print(subtext)
        if subtext.count('*')==0 and subtext.count('/')==0:
            try:
                result += float(subtext)
            except:
                result += 0
        elif subtext.count('/')==0:
            numbers = subtext.split('*')
            subresult = float(numbers[0])
            for i in range(1,len(numbers)):
                subresult *= float(numbers[i])
            result += subresult
        elif subtext.count('*')==0:
            numbers = subtext.split('/')
            subresult = float(numbers[0])
            for i in range(1,len(numbers)):
                subresult /= float(numbers[i])
            result += subresult
        else:
            numbers = subtext.split('*')
            subresult = 1
            for number in numbers:
                if number.count('/')==0:
                    subresult = subresult*float(number)
                else:
                    subnum = number.split('/')
                    sub = float(subnum[0])
                    for i in range(1,len(subnum)):
                        sub /= float(subnum[i])
                    subresult = subresult*sub
            result += subresult  

    et_result['text'] = et_result['text'] + f'\n={result}'

def btn_restartclick(event):
    et_result['text'] = '0'

def btn_delclick(event):
    if len(et_result['text'])==1:
        et_result['text'] = '0'
    elif et_result['text'] != '0':
        et_result['text'] = et_result['text'][:-1]

        
#menu
menubar = Menu(master=window)

viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)

editmenu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="Help", menu=helpmenu)

#result
et_result = Label(window,relief=RAISED, anchor="se", text='0',font=(textfont, 25))
et_result.grid(row=0,column=0,columnspan=5,padx=10,pady=10,sticky=NSEW)

#button
btn_MC = Button(window,text='MC',font=(textfont, fontbuttonsize))
btn_MC.grid(row=1,column=0,padx=(10,1),pady=1,sticky=NSEW)
btn_MC.bind('<Enter>', btn_enter)
btn_MC.bind('<Leave>', btn_leave)

btn_MR = Button(window,text='MR',font=(textfont, fontbuttonsize))
btn_MR.grid(row=1,column=1,padx=1,pady=1,sticky=NSEW)
btn_MR.bind('<Enter>', btn_enter)
btn_MR.bind('<Leave>', btn_leave)

btn_MS = Button(window,text='MS',font=(textfont, fontbuttonsize))
btn_MS.grid(row=1,column=2,padx=1,pady=1,sticky=NSEW)
btn_MS.bind('<Enter>', btn_enter)
btn_MS.bind('<Leave>', btn_leave)

btn_M1 = Button(window,text='M+',font=(textfont, fontbuttonsize))
btn_M1.grid(row=1,column=3,padx=1,pady=1,sticky=NSEW)
btn_M1.bind('<Enter>', btn_enter)
btn_M1.bind('<Leave>', btn_leave)

btn_M2 = Button(window,text='M-',font=(textfont, fontbuttonsize))
btn_M2.grid(row=1,column=4,padx=(1,10),pady=1,sticky=NSEW)
btn_M2.bind('<Enter>', btn_enter)
btn_M2.bind('<Leave>', btn_leave)

btn_del = Button(window,text='Del',font=(textfont, fontbuttonsize))
btn_del.grid(row=2,column=0,padx=(10,1),pady=1,sticky=NSEW)
btn_del.bind('<Enter>', btn_enter)
btn_del.bind('<Leave>', btn_leave)
btn_del.bind('<Button-1>', btn_delclick)

btn_CE = Button(window,text='CE',font=(textfont, fontbuttonsize))
btn_CE.grid(row=2,column=1,padx=1,pady=1,sticky=NSEW)
btn_CE.bind('<Enter>', btn_enter)
btn_CE.bind('<Leave>', btn_leave)

btn_C = Button(window,text='C',font=(textfont, fontbuttonsize))
btn_C.grid(row=2,column=2,padx=1,pady=1,sticky=NSEW)
btn_C.bind('<Enter>', btn_enter)
btn_C.bind('<Leave>', btn_leave)
btn_C.bind('<Button-1>', btn_restartclick)

btn_pl = Button(window,text='+-',font=(textfont, fontbuttonsize))
btn_pl.grid(row=2,column=3,padx=1,pady=1,sticky=NSEW)
btn_pl.bind('<Enter>', btn_enter)
btn_pl.bind('<Leave>', btn_leave)

btn_sqr = Button(window,text='√',font=(textfont, fontbuttonsize))
btn_sqr.grid(row=2,column=4,padx=(1,10),pady=1,sticky=NSEW)
btn_sqr.bind('<Enter>', btn_enter)
btn_sqr.bind('<Leave>', btn_leave)
btn_sqr.bind('<Button-1>', btn_click)

btn_7 = Button(window,text='7',font=(textfont, fontbuttonsize))
btn_7.grid(row=3,column=0,padx=(10,1),pady=1,sticky=NSEW)
btn_7.bind('<Enter>', btn_enter)
btn_7.bind('<Leave>', btn_leave)
btn_7.bind('<Button-1>', btn_click)

btn_8 = Button(window,text='8',font=(textfont, fontbuttonsize))
btn_8.grid(row=3,column=1,padx=1,pady=1,sticky=NSEW)
btn_8.bind('<Enter>', btn_enter)
btn_8.bind('<Leave>', btn_leave)
btn_8.bind('<Button-1>', btn_click)

btn_9 = Button(window,text='9',font=(textfont, fontbuttonsize))
btn_9.grid(row=3,column=2,padx=1,pady=1,sticky=NSEW)
btn_9.bind('<Enter>', btn_enter)
btn_9.bind('<Leave>', btn_leave)
btn_9.bind('<Button-1>', btn_click)

btn_division = Button(window,text='/',font=(textfont, fontbuttonsize))
btn_division.grid(row=3,column=3,padx=1,pady=1,sticky=NSEW)
btn_division.bind('<Enter>', btn_enter)
btn_division.bind('<Leave>', btn_leave)
btn_division.bind('<Button-1>', btn_click)

btn_per = Button(window,text='%',font=(textfont, fontbuttonsize))
btn_per.grid(row=3,column=4,padx=(1,10),pady=1,sticky=NSEW)
btn_per.bind('<Enter>', btn_enter)
btn_per.bind('<Leave>', btn_leave)
btn_per.bind('<Button-1>', btn_click)

btn_4 = Button(window,text='4',font=(textfont, fontbuttonsize))
btn_4.grid(row=4,column=0,padx=(10,1),pady=1,sticky=NSEW)
btn_4.bind('<Enter>', btn_enter)
btn_4.bind('<Leave>', btn_leave)
btn_4.bind('<Button-1>', btn_click)

btn_5 = Button(window,text='5',font=(textfont, fontbuttonsize))
btn_5.grid(row=4,column=1,padx=1,pady=1,sticky=NSEW)
btn_5.bind('<Enter>', btn_enter)
btn_5.bind('<Leave>', btn_leave)
btn_5.bind('<Button-1>', btn_click)

btn_6 = Button(window,text='6',font=(textfont, fontbuttonsize))
btn_6.grid(row=4,column=2,padx=1,pady=1,sticky=NSEW)
btn_6.bind('<Enter>', btn_enter)
btn_6.bind('<Leave>', btn_leave)
btn_6.bind('<Button-1>', btn_click)

btn_multiply = Button(window,text='*',font=(textfont, fontbuttonsize))
btn_multiply.grid(row=4,column=3,padx=1,pady=1,sticky=NSEW)
btn_multiply.bind('<Enter>', btn_enter)
btn_multiply.bind('<Leave>', btn_leave)
btn_multiply.bind('<Button-1>', btn_click)

btn_divisionx = Button(window,text='1/x',font=(textfont, fontbuttonsize))
btn_divisionx.grid(row=4,column=4,padx=(1,10),pady=1,sticky=NSEW)
btn_divisionx.bind('<Enter>', btn_enter)
btn_divisionx.bind('<Leave>', btn_leave)

btn_1 = Button(window,text='1',font=(textfont, fontbuttonsize))
btn_1.grid(row=5,column=0,padx=(10,1),pady=1,sticky=NSEW)
btn_1.bind('<Enter>', btn_enter)
btn_1.bind('<Leave>', btn_leave)
btn_1.bind('<Button-1>', btn_click)

btn_2 = Button(window,text='2',font=(textfont, fontbuttonsize))
btn_2.grid(row=5,column=1,padx=1,pady=1,sticky=NSEW)
btn_2.bind('<Enter>', btn_enter)
btn_2.bind('<Leave>', btn_leave)
btn_2.bind('<Button-1>', btn_click)

btn_3 = Button(window,text='3',font=(textfont, fontbuttonsize))
btn_3.grid(row=5,column=2,padx=1,pady=1,sticky=NSEW)
btn_3.bind('<Enter>', btn_enter)
btn_3.bind('<Leave>', btn_leave)
btn_3.bind('<Button-1>', btn_click)

btn_minus = Button(window,text='-',font=(textfont, fontbuttonsize))
btn_minus.grid(row=5,column=3,padx=1,pady=1,sticky=NSEW)
btn_minus.bind('<Enter>', btn_enter)
btn_minus.bind('<Leave>', btn_leave)
btn_minus.bind('<Button-1>', btn_click)

btn_equal = Button(window,text='=',font=(textfont, fontbuttonsize))
btn_equal.grid(row=5,rowspan=2,column=4,padx=(1,10),pady=(1,10),sticky=NSEW)
btn_equal.bind('<Enter>', btn_enter)
btn_equal.bind('<Leave>', btn_leave)
btn_equal.bind('<Button-1>', btn_equalclick)

btn_0 = Button(window,text='0',font=(textfont, fontbuttonsize))
btn_0.grid(row=6,columnspan=2,column=0,padx=(10,1),pady=(1,10),sticky=NSEW)
btn_0.bind('<Enter>', btn_enter)
btn_0.bind('<Leave>', btn_leave)
btn_0.bind('<Button-1>', btn_click)

btn_dot = Button(window,text='.',font=(textfont, fontbuttonsize))
btn_dot.grid(row=6,column=2,padx=1,pady=(1,10),sticky=NSEW)
btn_dot.bind('<Enter>', btn_enter)
btn_dot.bind('<Leave>', btn_leave)
btn_dot.bind('<Button-1>', btn_click)

btn_plus = Button(window,text='+',font=(textfont, fontbuttonsize))
btn_plus.grid(row=6,column=3,padx=1,pady=(1,10),sticky=NSEW)
btn_plus.bind('<Enter>', btn_enter)
btn_plus.bind('<Leave>', btn_leave)
btn_plus.bind('<Button-1>', btn_click)

window.config(menu=menubar)
window.mainloop()