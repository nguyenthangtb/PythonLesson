from math import sqrt

print("Giai phuong trinh bac 2 => ax^2 +bx + c = 0")
a = float(input("Nhap a => "))
b = float(input("Nhap b => "))
c = float(input("Nhap c => "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo nghiem!")
        else:
            print("Phuong trinh vo nghiem")
    else:
        if c == 0:
            print("Phuong trinh co nghiem x = 0")
        else:
            print("Phuong trinh co nghiem x =", -c/b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("phuong trinh vo nghiem!")
    elif delta == 0:
        print("Phuong trinh co 1 nghiem x = ", -b/(2*a))
    else:
        print("Phuong trinh co 2 nghiem phan biet!")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))    
