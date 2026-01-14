import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input('\nNhấn Enter để tiếp tục...\n')

students={}
def add_students():
    clear()
    while True:
        try:
            id=int(input('Nhập mã số sinh viên: '))
            if id not in students:
                 break
            else:
                 print('Mã số sinh viên đã tồn tại\n')
        except ValueError:
            print('MSSV không hợp lệ\n')
    clear()
    
    tên=input('Họ và tên: ')
    clear()    
    
    while True:
        try: 
            quizz=float(input('Quizz: '))
            if 0<quizz<=10.0:
             break
            else:
             print('Điểm phải từ 0 đến 10\n')
        except ValueError:
            print('Vui lòng nhập số\n')
        
    while True:
        try: 
            test1=float(input('Test 1: '))
            if 0<test1<=10.0:
             break
            else:
             print('Điểm phải từ 0 đến 10\n')
        except ValueError:
            print('Vui lòng nhập số\n')
        
    while True:
        try: 
            test2=float(input('Test 2: '))
            if 0<test2<=10.0:
             break
            else:
             print('Điểm phải từ 0 đến 10\n')
        except ValueError:
            print('Vui lòng nhập số\n')
    
    while True:
        try: 
            test3=float(input('Test 3: '))
            if 0<test3<=10.0:
             break
            else:
             print('Điểm phải từ 0 đến 10\n')
        except ValueError:
            print('Vui lòng nhập số\n')
    
    while True:
        try: 
            mid_term=float(input('Mid Term: '))
            if 0<mid_term<=10.0:
             break
            else:
             print('Điểm phải từ 0 đến 10\n')
        except ValueError:
            print('Vui lòng nhập số\n')

    while True:
        try: 
            final=float(input('Final: '))
            if 0<final<=10.0:
             break
            else:
             print('Điểm phải từ 0 đến 10\n')
        except ValueError:
            print('Vui lòng nhập số\n')
    
    tb_hs1=(quizz+test1+test2+test3)/4
    score=tb_hs1*0.16+mid_term*0.24+final*0.6
    total=f'{score:.1f}'
    
    students[id]={'Họ và tên':tên,'Quizz':quizz,'Test 1':test1,'Test 2':test2,'Test 3':test3,'Mid term':mid_term,'Final':final,'Average':total}
    clear()
    print('Đã thêm sinh viên')
    pause()

def find_students():
    clear()
    mssv=int(input('Nhập mã số sinh viên:'))
    if mssv not in students:
         print('Không tìm thấy sinh viên')
    else:
         clear()
         print(f"{'MSSV':<10}{'Họ và tên':<20}{'Quizz':<10}{'Test 1':<11}{'Test 2':<11}{'Test 3':<11}{'Mid term':<14}{'Final':<10}{'Average':<10}")
         info=students[mssv]
         print(f"{mssv:<10}{info['Họ và tên']:<20}{info['Quizz']:<10}{info['Test 1']:<11}{info['Test 2']:<11}{info['Test 3']:<11}{info['Mid term']:<14}{info['Final']:<10}{info['Average']:<10}")
    pause()

def delete_students():
    clear()
    b=int(input('Nhập MSSV: '))
    if b in students:
            students.pop(b)
            print('Đã xóa sinh viên')
    else:
            print('Không tìm thấy sinh viên')
    pause()

def show_students():
     if not students:
          clear()
          print('Danh sách trống')
     else:
          clear()
          print(f"{'MSSV':<10}{'Họ và tên':<20}{'Quizz':<10}{'Test 1':<11}{'Test 2':<11}{'Test 3':<11}{'Mid term':<14}{'Final':<10}{'Average':<10}")
          for mssv,info in students.items():
           print(f"{mssv:<10}{info['Họ và tên']:<20}{info['Quizz']:<10}{info['Test 1']:<11}{info['Test 2']:<11}{info['Test 3']:<11}{info['Mid term']:<14}{info['Final']:<10}{info['Average']:<10}")
     pause()

while True:
    clear()
    print('1.Thêm sinh viên')
    print('2.Tìm sinh viên')
    print('3.Xem danh sách sinh viên')
    print('4.Xóa sinh viên')
    print('5.Thoát chương trình')
    try:
        a=int(input('Nhập lựa chọn của bạn: '))
        if a<1 or a>5:
            print('0')
            continue
    except ValueError:
        continue
    if a==1:
        add_students()
    elif a==2:
        find_students()
    elif a==3:
        show_students()
    elif a==4:
         delete_students()
    elif a==5:
         break

     