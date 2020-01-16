import sys


# Nhap vao danh sach sinh vien
students = []
num = print("So luong sv muon nhap: ")

num  = int(input())

for student in range(num):
    _hoten = input("Enter hoten: ")
    _diem = int(input("Enter diem: "))
    _gioitinh = input("Enter sex: ")
    # while True:
    #     if(_diem > 10):
    #         print("Diem khong > 10")
    #         continue 
    #     else:
    #         _diem = int(input("Enter diem: "))   
    #         break

    students.append((_hoten, _diem, _gioitinh))

while True:
    output = int(input(
        "Nhap co phim chuc nang sau de su dung chuong trinh\n1 => Ds sinh vien > 8\n2 => Ds sinh vien\n0 => thoat "))
    if output == 1:
        print("=== Ho va Ten ============= Diem ================ Gioi tinh")
        for i, j, k in students:
            if(j >= 8):
                print("===", str.upper(i),        j,      k)
            else:
                print("khong co")
                break
        continue
    elif output == 2:
        print("=== Ho va Ten =========== Diem")
        for i, j, k in students:
            print("===", str.upper(i),           j,    k)
        continue
    elif output == 0:
        sys.exit()
