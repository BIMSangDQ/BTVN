class Student:
    def __init__(self,code,name,dateofbirth,residence):
        self.code = code
        self.name = name
        self.dateofbirth = dateofbirth
        self.residence = residence
        
    def info(self):
        print(f'{str(self.code).ljust(10)}{str(self.name).ljust(30)}'+\
             f'{str(self.dateofbirth).ljust(20)}{self.residence}' )
        
    def print_header(self):
        header = 'Mã Sv'.ljust(10)+'Họ tên'.ljust(30)+'Ngày sinh'.ljust(20)+'Quê quán'
        print(header)
        print(''.ljust(80,'='))

from datetime import datetime
class List_Student:
    def __init__(self,students):
        self.students = students
    
    def load(self):
        stud1 = Student('57228','Đặng Quang Sáng','28/02/1993','Bình Định')
        stud2 = Student('57227','Đặng Hoàng Vũ','06/09/1992','Nghệ An')
        stud3 = Student('57229','Nguyễn Thị Lưu Ý Nhi','29/03/1992','Daklak')
        stud4 = Student('57230','Tạ Đình Huy','29/03/1997','Bình Thuận')
        self.students = [stud1,stud2,stud3,stud4]
        
    def add_student(self,student):
        self.students.append(student)
        student.print_header()
        student.info()
        print('Thêm thông tin sinh viên thành công')
        print(''.ljust(100,'='))
        
    def delete_student(self,code):
        for stud in self.students:
            if stud.code == code:
                self.students.remove(stud)
                print('Xóa thông tin sinh viên thành công')
                return
        print("Sinh viên cần xóa không tồn tại")
        
    def update_student(self,student):
        for stud in self.students:
            if stud.code == student.code:
                if student.name!= "": stud.name = student.name
                if student.dateofbirth!= "": stud.dateofbirth = student.dateofbirth
                if student.residence!= "": stud.residence = student.residence
                print('Cập nhật thông tin sinh viên thành công')
                stud.print_header()
                stud.info()
                print(''.ljust(100,'='))
                return
        confirm = input('Không tìm thấy mã sinh viên cần cập nhật! \n Bạn có muốn thêm mới (y/n)')
        if confirm.upper() == 'Y':
            self.add_student(student)
        
    def find(self,_str,option):
        list_result = []
        columnname = ''
        if option == '1':
            columnname = 'cột "Mã sinh viên'
            for stud in self.students:
                if stud.code.upper().find(_str.upper()) >= 0:
                    list_result.append(stud)
        elif option == '2':
            columnname = 'cột "Tên sinh viên'
            for stud in self.students:
                if stud.name.upper().find(_str.upper()) >= 0:
                    list_result.append(stud)
        elif option == '3':
            columnname ='cột "Ngày sinh'
            for stud in self.students:
                if stud.dateofbirth.upper().find(_str.upper()) >= 0:
                    list_result.append(stud)
        elif option == '4':
            columnname ='cột "Quê quán'
            for stud in self.students:
                if stud.residence.upper().find(_str.upper()) >= 0:
                    list_result.append(stud)
        else:
            columnname ='tất cả các cột'
            for stud in self.students:
                if stud.code.upper().find(_str.upper()) >= 0:
                    list_result.append(stud)
                    continue
                elif stud.name.upper().find(_str.upper()) >= 0:
                    list_result.append(stud)
                    continue
                elif stud.dateofbirth.upper().find(_str.upper()) >= 0:
                    list_result.append(stud)
                    continue
                elif stud.residence.upper().find(_str.upper()) >= 0:
                    list_result.append(stud)
                    continue
        print(f'Kết quả tìm kiếm trong {columnname}" với từ khóa: "{_str}"')
        print(f'Có {len(list_result)} kết quả:')
        for i in range(0,len(list_result),1):
            if i == 0:
                list_result[i].print_header()
            list_result[i].info()
        print()
        print(''.ljust(100,'='))
        
    def sort_by(self,option,isreverse):
        if option == '2':
            list_result = sorted(self.students,key = lambda x: x.name,reverse = isreverse)
        elif option == '3':
            list_result = sorted(self.students,\
                        key = lambda x: datetime.strptime(x.dateofbirth, "%d/%m/%Y").strftime("%Y-%m-%d"),reverse = isreverse)
        elif option == '4':
            list_result = sorted(self.students,key = lambda x: x.residence,reverse = isreverse)
        else:
            list_result = sorted(self.students,key = lambda x: x.code,reverse = isreverse)
            
        for i in range(0,len(list_result),1):
            if i == 0:
                list_result[i].print_header()
            list_result[i].info()
        print()
        print(''.ljust(100,'='))
        
    def info(self):
        header = 'Mã Sv'.ljust(10)+'Họ tên'.ljust(30)+'Ngày sinh'.ljust(20)+'Quê quán'
        print(header)
        print(''.ljust(80,'='))
        for stud in self.students:
            stud.info()
        print()
        print(''.ljust(100,'='))

from datetime import datetime
class Program:
    def __init__(self):
        self.dssv = List_Student(None)
        self.dssv.load()
        
    def validate_dateformat(self,date_input):
        try:
            date_input = datetime.strptime(date_input,"%d/%m/%Y")
            return True
        except:
            print('Lỗi nhập dữ liệu, vui lòng nhập lại!')
            return False
        
    def check_exitscode(self,code):
        success = True
        for stud in self.dssv.students:
            if stud.code == code:
                print('Mã sinh viên đã tồn tại, vui lòng nhập lại!')
                success = False
                break
        return success
    
    def format_name(self,_str):
        _str = _str.lower().strip().split()
        i=0
        Name = ''
        while i < len(_str):
            Name += " "+_str[i][0].upper()+_str[i][1:].lower()
            i+=1
        return (Name.lstrip())
    
    def run(self):
        while 1:
            print()
            print('============ Quản lý sinh viên ============')
            print('=== 1. Hiển thị danh sách               ===')
            print('=== 2. Thêm sinh viên                   ===')
            print('=== 3. Chỉnh sửa thông tin sinh viên    ===')
            print('=== 4. Xóa thông tin                    ===')
            print('=== 5. Tìm kiếm thông tin               ===')
            print('=== 6. Sắp xếp học sinh                 ===')
            print('=== 7. Đóng chương trình                ===')
            print('===========================================')

            choice = input('Nhập lựa chọn: ').strip()
            checklist = '1 2 3 4 5 6 7'
            if checklist.find(choice)<0 or choice == '':
                print('Lựa chọn không hợp lệ! Vui lòng lựa chọn lại')
            print()
            
            if choice == '1':
                self.dssv.info()
            elif choice == '2':
                while 1:
                    code = input('Nhập mã sinh viên: ')
                    if self.check_exitscode(code):
                        break
                name = self.format_name(input('Nhập tên sinh viên: '))
                while 1:
                    dateofbirth = input('Nhập ngày sinh (dd/mm/yyy): ')
                    if self.validate_dateformat(dateofbirth):
                        break
                residence = self.format_name(input('Nhập quê quán: '))
                stud = Student(code,name,dateofbirth,residence)
                self.dssv.add_student(stud)
            elif choice == '3':
                code = input('Nhập mã sinh viên: ')
                name = input('Nhập tên sinh viên: ')
                while 1:
                    dateofbirth = input('Nhập ngày sinh (dd/mm/yyy): ')
                    if dateofbirth == '': break
                    if self.validate_dateformat(dateofbirth):
                        break
                residence = input('Nhập quê quán: ')
                stud = Student(code,name,dateofbirth,residence)
                self.dssv.update_student(stud)
            elif choice == '4':
                deleting = input('Nhập mã sinh viên cần xóa: ')
                self.dssv.delete_student(deleting)
            elif choice == '5':
                print('=================== 5. Tìm kiếm thông tin ================')
                print('==== 1. Tìm theo mã sinh viên                          ===')
                print('==== 2. Tìm theo họ tên sinh viên                      ===')
                print('==== 3. Tìm theo ngày sinh                             ===')
                print('==== 4. Tìm theo quê quán                              ===')
                print('==== 5. Tìm trong tất cả các trường thông tin (defaut) ===')
                print('==========================================================')
                option = input('Nhập lựa chọn tìm kiếm :')
                textfind = input('Nhập từ khóa tìm kiếm :')
                print()
                self.dssv.find(textfind.strip(),option.strip())
            elif choice == '6':
                print('=================== 6. Sắp xếp thông tin ================')
                print('==== 1. Sắp xếp theo mã sinh viên (defaut)            ===')
                print('==== 2. Sắp xếp theo họ tên sinh viên                 ===')
                print('==== 3. Sắp xếp theo ngày sinh                        ===')
                print('==== 4. Sắp xếp theo quê quán                         ===')
                print('=========================================================')
                option = input('Nhập lựa chọn sắp xếp : ')
                reverse = input('Sắp xếp tăng dần: (1/0): ')
                print()
                if reverse == '0':
                    isreverse = True
                else:
                    isreverse = False
                self.dssv.sort_by(option.strip(),isreverse)
            elif choice == '7':
                confirm = input('Bạn muốn đóng chương trình (y/n)?')
                if confirm == 'y' or confirm == 'Y':
                    break
            
            input('Nhấn enter để tiếp tục....')
        print('Kết thúc chương trình')

main = Program()
main.run()