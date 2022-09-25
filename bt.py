from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x200")
window.resizable(0,0)

highlightcolor = 'lightblue'
textfont = "Helvetica"
textheight = 12
textheight_warning = 8

def btn_Run(event):
    for char in et_number1.get():
        if char.isalpha():
            lb_result["text"]= 'error'
            return

    for char in et_number2.get():
        if char.isalpha():
            lb_result["text"]= 'error'
            return

    lb_result["text"] = float(et_number1.get()) + float(et_number2.get())

def check_number1(event):
    for char in et_number1.get():
        if char.isalpha():
            lb_number1_warning["text"] = 'Number 1 is fail'
            break
    lb_number1_warning["text"] = ''

def reset_number1(event):
    lb_number1_warning["text"] = ''

def check_number2(event):
    for char in et_number2.get():
        if char.isalpha():
            lb_number2_warning["text"] = 'Number 2 is fail'
            break
    lb_number2_warning["text"] = ''

def reset_number2(event):
    lb_number2_warning["text"] = ''

window.columnconfigure(0,weight = 1)
window.columnconfigure(1,weight = 1)
window.columnconfigure(2,weight = 1)

window.rowconfigure(0,weight = 2)
window.rowconfigure(1,weight = 1)
window.rowconfigure(2,weight = 2)
window.rowconfigure(3,weight = 1)
window.rowconfigure(4,weight = 2)

lb_number1 = Label(window, anchor="w", text='Number 1',font=(textfont, textheight))
lb_number1.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)

et_number1 = Entry(window,font=(textfont, textheight))
et_number1.grid(row=0,column=1,columnspan=2,padx=10,pady=10,sticky=NSEW)
et_number1.bind("<FocusOut>",check_number1)
et_number1.bind("<FocusIn>",reset_number1)

lb_number1_warning = Label(window, anchor="w",fg='red', text='',font=(textfont, textheight_warning))
lb_number1_warning.grid(row=1,column=1,columnspan=2,sticky=NSEW)

lb_number2 = Label(window, anchor="w", text='Number 2',font=(textfont, textheight))
lb_number2.grid(row=2,column=0,padx=10,pady=10,sticky=NSEW)

et_number2 = Entry(window,font=(textfont, textheight))
et_number2.grid(row=2,column=1,columnspan=2,padx=10,pady=10,sticky=NSEW)
et_number2.bind("<FocusOut>",check_number2)
et_number2.bind("<FocusIn>",reset_number2)

lb_number2_warning = Label(window, anchor="w",fg='red', text='',font=(textfont, textheight_warning))
lb_number2_warning.grid(row=3,column=1,columnspan=2,sticky=NSEW)

lb_result = Label(window, anchor="w",bg='#cce7e8',fg='green',font=(textfont, textheight))
lb_result.grid(row=4,column=1,pady=10,sticky=NSEW)

btn_run = Button(window,text="SUM",bg='lightblue')
btn_run.grid(row=4,column=2,padx=10,pady=10,sticky=NSEW)
btn_run.bind("<Button-1>",btn_Run)

window.mainloop()