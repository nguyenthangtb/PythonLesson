import sys


# Nhap vao danh sach sinh vien
students = []
num = 2
for student in range(num):
    _hoten = input("Enter hoten: ")
    _diem = int(input("Enter diem: "))
    while True:
        if(_diem > 10):
            print("Diem khong > 10")
            continue 
        else:
            _diem = int(input("Enter diem: "))   
            break

    students.append((_hoten, _diem))

while True:
    output = int(input(
        "Nhap co phim chuc nang sau de su dung chuong trinh\n1 => Ds sinh vien > 8\n2 => Ds sinh vien\n0 => thoat "))
    if output == 1:
        print("=== Ho va Ten ============= Diem")
        for i, j in students:
            if(j >= 8):
                print("===", str.upper(i),        j, "Loai gioi")
            else:
                print("khong co")
                break
        continue
    elif output == 2:
        print("=== Ho va Ten =========== Diem")
        for i, j in students:
            print("===", str.upper(i),           j, "Loai TB")
        continue
    elif output == 0:
        sys.exit()
