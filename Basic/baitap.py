# Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) 
# (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. Với giá trị cố định của C là 50, H là 30. 
# D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.
# Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
import math
def canbachai():
    c = 50
    h = 30
    value = []

    items = [
        
        item for item in input("Nhập giá trị của d: ").split(',')
    ]
    for d in items:
        value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
    print(' , '.join(value))    
#canbachai()


# Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, 
# phân tách nhau bởi dấu phẩy và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.

def chuoinguoidung():
    strs = []

    for item in item:
        input("Nhap chuoi: ".split(","))
        strs.append(item)

    # strs = [
    #     item for item in input("nhap chuoi: ").split(',')
    # ]

    strs.sort()
    print(" , ".join(strs))


chuoinguoidung()