from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import pyodbc

root = Tk()
root.title('QL_THƯ VIỆN')
root.geometry('620x870')
root.resizable(False, False)
root.configure(bg='white')

#region variable
bookid = IntVar()
bookid.set(0)

bookName = StringVar()
bookName.set("")

category = StringVar()
category.set("")

yearOfPub = IntVar()
yearOfPub.set(0)

pagenumber = IntVar()
pagenumber.set(0)

company = StringVar()
company.set("")

price = IntVar()
price.set(0)

operator  = StringVar()
operator.set("")

cproperty  = StringVar()
cproperty.set("")

condition  = StringVar()
condition.set("")

valueen  = StringVar()
valueen.set("")
#endregion

#region method
def SQLConnect():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-OQLFA92\SANGDANG;'
                        'Database=COVID19;'
                        'Trusted_Connection=yes;')
    return conn

def List_allbook():
    conn = SQLConnect()
    query = """
    select Lb_book.id,book_name,category_name,year_of_public,page_number,[Lb_Company].name,price
    from (Lb_book INNER JOIN Lb_Category ON category_id = [Lb_Category].id)
    INNER JOIN Lb_Company ON publis_company_id = [Lb_Company].id
    """
    cursor = conn.cursor()
    cursor.execute(query)
    books = cursor.fetchall()
    book_list = []
    for b in books:
        s = []
        for i in range(1,7):
            s.append(b[i])
        s.append(b[0])
        book_list.append(s)
    conn.close()
    return book_list

def List_book_with_condition(condition):
    conn = SQLConnect()
    query = """
    select Lb_book.id,book_name,category_name,year_of_public,page_number,[Lb_Company].name,price
    from (Lb_book INNER JOIN Lb_Category ON category_id = [Lb_Category].id)
    INNER JOIN Lb_Company ON publis_company_id = [Lb_Company].id
    """
    cursor = conn.cursor()
    cursor.execute(query+" WHERE "+condition)
    books = cursor.fetchall()
    book_list = []
    for b in books:
        s = []
        for i in range(1,7):
            s.append(b[i])
        s.append(b[0])
        book_list.append(s)
    conn.close()
    return book_list

def add_book2tree_with_condition(condition):
    books = List_book_with_condition(condition)
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert('', END, values=book)

def add_book2tree():
    books = List_allbook()
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert('', END, values=book)

def List_Category():
    conn = SQLConnect()
    query = """
    select * from Lb_Category
    """
    cursor = conn.cursor()
    cursor.execute(query)
    categories = cursor.fetchall()
    category_list = []
    for c in categories:
        category_list.append(c[1])
    conn.close()
    return category_list  

def List_Company():
    conn = SQLConnect()
    query = """
    select * from Lb_Company
    """
    cursor = conn.cursor()
    cursor.execute(query)
    companies = cursor.fetchall()
    company_list = []
    for c in companies:
        company_list.append(c[1])
    conn.close()
    return company_list  

def btn_enter(event):
    event.widget['bg']= 'skyblue'

def btn_leavecyan(event):
    event.widget['bg']='cyan'

def btn_leavered(event):
    event.widget['bg']='red'

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        break
    bookName.set(record[0])
    category.set(record[1])
    yearOfPub.set(record[2])
    pagenumber.set(record[3])
    company.set(record[4])
    price.set(record[5])
    bookid.set(record[6])

def get_categoryID():
    conn = SQLConnect()
    categoryid = 0
    category_sql = f"SELECT * FROM Lb_Category WHERE category_name = N'{category.get()}'"
    cursor = conn.cursor()
    cursor.execute(category_sql)
    categories = cursor.fetchall()
    for c in categories:
        categoryid = int(c[0])
    conn.close()
    return categoryid

def get_companyID():
    conn = SQLConnect()
    companyID = 0
    category_sql = f"SELECT * FROM Lb_Company WHERE Lb_Company.name = N'{company.get()}'"
    cursor = conn.cursor()
    cursor.execute(category_sql)
    companies = cursor.fetchall()
    for c in companies:
        companyID = int(c[0])
    conn.close()
    return companyID

def btn_addbookev():
    categoryid = get_categoryID()
    companyid = get_companyID()

    conn = SQLConnect()
    query = """
    INSERT INTO Lb_book (book_name,category_id,year_of_public,page_number,publis_company_id,price)
    VALUES (?,?,?,?,?,?)
    """
    cursor = conn.cursor()
    cursor.execute(query,bookName.get(),categoryid,yearOfPub.get(),pagenumber.get(),companyid,price.get())
    cursor.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo(title='Admin',message='Thêm thành công')
    add_book2tree()

def btn_editbookev():
    categoryid = get_categoryID()
    companyid = get_companyID()
    print(bookid.get())
    conn = SQLConnect()
    query = """
    UPDATE Lb_book SET 
    book_name=?,
    category_id=?,
    year_of_public=?,
    page_number=?,
    publis_company_id=?,
    price=?
    WHERE id = ?
    """
    cursor = conn.cursor()
    cursor.execute(query,bookName.get(),categoryid,yearOfPub.get(),pagenumber.get(),companyid,price.get(),bookid.get())
    cursor.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo(title='Admin',message='Cập nhật thành công')
    add_book2tree()

def btn_delbookev():
    MsgBox = messagebox.askquestion ('Admin',f'Bạn muốn xóa cuốn sách {bookName.get()} này không?')
    if MsgBox == 'yes':
        conn = SQLConnect()
        query = "DELETE FROM Lb_book WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query,bookid.get())
        cursor.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo(title='Admin',message='Xóa thành công thành công')
        add_book2tree()
    else:
        return

def btn_addfilter():
    filter = [operator.get(),cproperty.get(),condition.get(),valueen.get()]
    tree2.insert('', END, values=filter)

def btn_clearfilter():
    tree2.delete(*tree2.get_children())
    add_book2tree()

def btn_filter():
    condition_list = []
    for child in tree2.get_children():
        condition_list.append(tree2.item(child)["values"])

    if len(condition_list) == 0:
        add_book2tree()
    else:
        property_list = ['Lb_book.id','book_name','category_name','year_of_public','page_number','[Lb_Company].name','price' ]
        cproperty_list = ['Tên sách','Thể loại','Năm XB','Số trang','NXB','Giá']
        count = 0
        condition_string = "("
        for c in condition_list:
            if c[0] == 'Or':
                condition_string += ") or ("
                count = 0
            else:
                if count > 0:
                    condition_string += " and "
        
            cproperty_list.index(c[1])
            condition_string += property_list[cproperty_list.index(c[1])+1]
            
            if c[2] == 'Có chứa từ':
                condition_string += f" LIKE N'%{c[3]}%'"
            else:
                condition_string += f" {c[2]} {c[3]}" 
            count += 1
        condition_string += ")"
        print(condition_string)

        add_book2tree_with_condition(condition_string)
#endregion

#region view
frame_book = LabelFrame( root, text="Quản lý sách",bg='white', bd=5, font=("Helvetica", 12))
frame_book.grid(row=0,column=0, sticky=NSEW,padx=5,pady=5)

lbl_bookname=Label(frame_book, text="Tên sách", fg='black',bg='white', font=("Helvetica", 12))
lbl_bookname.grid(row=0,column=0, sticky=W)

lbl_category=Label(frame_book, text="Thể loại", fg='black',bg='white', font=("Helvetica", 12))
lbl_category.grid(row=1,column=0, sticky=W)

lbl_year_ofpub=Label(frame_book, text="Năm xuất bản", fg='black',bg='white', font=("Helvetica", 12))
lbl_year_ofpub.grid(row=2,column=0, sticky=W)

lbl_pagenumber=Label(frame_book, text="Số trang", fg='black',bg='white', font=("Helvetica", 12))
lbl_pagenumber.grid(row=3,column=0, sticky=W)

lbl_company=Label(frame_book, text="Nhà xuất bản", fg='black',bg='white', font=("Helvetica", 12))
lbl_company.grid(row=4,column=0, sticky=W)

lbl_price=Label(frame_book, text="Giá tiền (VNĐ)", fg='black',bg='white', font=("Helvetica", 12))
lbl_price.grid(row=5,column=0, sticky=W)

en_book=Entry(frame_book, textvariable=bookName, bd=2, width=50, font=("Helvetica", 12))
en_book.grid(row=0,column=1, sticky=W,padx=20,pady=5 )

cb_category=Combobox(frame_book, textvariable=category, width=48, font=("Helvetica", 12))
cb_category["values"] = List_Category()
cb_category.grid(row=1,column=1, sticky=W,padx=20,pady=5 )

en_year=Entry(frame_book, textvariable=yearOfPub, bd=2, width=50, font=("Helvetica", 12))
en_year.grid(row=2,column=1, sticky=W,padx=20,pady=5 )

en_pagenumber=Entry(frame_book, textvariable=pagenumber, bd=2, width=50, font=("Helvetica", 12))
en_pagenumber.grid(row=3,column=1, sticky=W,padx=20,pady=5 )

cb_company=Combobox(frame_book, textvariable=company, width=48, font=("Helvetica", 12))
cb_company["values"] = List_Company()
cb_company.grid(row=4,column=1, sticky=W,padx=20,pady=5 )

en_price=Entry(frame_book, textvariable=price, bd=2, width=50, font=("Helvetica", 12))
en_price.grid(row=5,column=1, sticky=W,padx=20,pady=5 )

btn_addbook = Button(frame_book,bg='white',width=10,text='THÊM SÁCH',background='cyan',font=("Helvetica", 12))
btn_addbook.grid(row=6,column=1,sticky=W,padx=20,pady=10)
btn_addbook["command"]=btn_addbookev
btn_addbook.bind('<Enter>',btn_enter)
btn_addbook.bind('<Leave>',btn_leavecyan)

btn_editbook = Button(frame_book,bg='white',width=10,text='SỬA SÁCH',background='cyan',font=("Helvetica", 12))
btn_editbook.grid(row=6,column=1,sticky=N,pady=10)
btn_editbook["command"]=btn_editbookev
btn_editbook.bind('<Enter>',btn_enter)
btn_editbook.bind('<Leave>',btn_leavecyan)

btn_delbook = Button(frame_book,bg='white',width=10,text='XÓA',background='red',font=("Helvetica", 12))
btn_delbook.grid(row=6,column=1,sticky=E,padx=20,pady=10)
btn_delbook["command"]=btn_delbookev
btn_delbook.bind('<Enter>',btn_enter)
btn_delbook.bind('<Leave>',btn_leavered)

#result
frame_result = LabelFrame( root, text="Kết quả",bg='white', bd=5, font=("Helvetica", 12))
frame_result.grid(row=1,column=0, sticky=NSEW,padx=5,pady=5)

columns = ('Tên sách', 'Thể loại', 'Năm XB', 'Số trang', 'NXB', 'Giá')
tree = ttk.Treeview(frame_result, columns=columns, show='headings')
tree.heading('Tên sách', text='Tên sách')
tree.column('Tên sách', minwidth=0, width=220, stretch=NO)
tree.heading('Thể loại', text='Thể loại')
tree.column('Thể loại', minwidth=0, width=100, stretch=NO)
tree.heading('Năm XB', text='Năm XB')
tree.column('Năm XB', minwidth=0, width=60, stretch=NO)
tree.heading('Số trang', text='Số trang')
tree.column('Số trang', minwidth=0, width=60, stretch=NO)
tree.heading('NXB', text='NXB')
tree.column('NXB', minwidth=0, width=70, stretch=NO)
tree.heading('Giá', text='Giá')
tree.column('Giá', minwidth=0, width=65, stretch=NO)
tree.grid(row=0, column=0,columnspan=6, sticky=NSEW)
add_book2tree()
tree.bind('<<TreeviewSelect>>', item_selected)
scrollbar = ttk.Scrollbar(frame_result, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=6, sticky='ns')

btn_viewall = Button(frame_result,bg='white',background='cyan',width=10,text='Tìm kiếm',font=("Helvetica", 12))
btn_viewall.grid(row=1,column=0,sticky=W,padx=10,pady=10)
btn_viewall['command']= btn_filter
btn_viewall.bind('<Enter>',btn_enter)
btn_viewall.bind('<Leave>',btn_leavecyan)

cb_Operator=Combobox(frame_result, textvariable=operator, width=10)
cb_Operator["values"] = ['          And','Or']
cb_Operator.grid(row=2,column=0, sticky=NSEW,pady=5 )

cb_Property=Combobox(frame_result, textvariable=cproperty, width=10)
cb_Property["values"] = ['Tên sách','Thể loại','Năm XB','Số trang','NXB','Giá']
cb_Property.grid(row=2,column=1, sticky=NSEW,pady=5 )

cb_Condition=Combobox(frame_result, textvariable=condition, width=10)
cb_Condition["values"] = ['Có chứa từ','=','>','>=','<','<=']
cb_Condition.grid(row=2,column=2, sticky=NSEW,pady=5 )

en_value=Entry(frame_result, textvariable=valueen, bd=2)
en_value.grid(row=2,column=3, sticky=NSEW,pady=5 )

btn_add = Button(frame_result,bg='white',background='cyan',text='Thêm đk',font=("Helvetica", 10))
btn_add.grid(row=2,column=4,sticky=NSEW,pady=5)
btn_add["command"] = btn_addfilter
btn_add.bind('<Enter>',btn_enter)
btn_add.bind('<Leave>',btn_leavecyan)

btn_del = Button(frame_result,bg='white',background='red',text='Xóa đk',font=("Helvetica", 10))
btn_del.grid(row=2,column=5, columnspan=2,sticky=NSEW,pady=5)
btn_del["command"] =btn_clearfilter
btn_del.bind('<Enter>',btn_enter)
btn_del.bind('<Leave>',btn_leavered)

columnscondition = ('Operator','Property','Condition','Value')
tree2 = ttk.Treeview(frame_result, columns=columnscondition, show='headings')
tree2.heading('Operator', text='Operator')
tree2.column('Operator', minwidth=0, width=100, stretch=NO)
tree2.heading('Property', text='Property')
tree2.column('Property', minwidth=0, width=100, stretch=NO)
tree2.heading('Condition', text='Condition')
tree2.column('Condition', minwidth=0, width=150, stretch=NO)
tree2.heading('Value', text='Value')
tree2.column('Value', minwidth=0, width=200, stretch=NO)
tree2.grid(row=3, column=0,columnspan=6, sticky=NSEW)

scrollbar = ttk.Scrollbar(frame_result, orient=VERTICAL, command=tree2.yview)
tree2.configure(yscroll=scrollbar.set)
scrollbar.grid(row=3, column=6, sticky='ns')
#endregion
root.mainloop()