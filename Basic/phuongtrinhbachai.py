from math import sqrt

# phuong trinh bac 2
# cong thuc => delta = b2 - 4ac
# TH1 => delta < 0 => phuong trinh vo nghiem
# TH2 => delta  == 0 phuong trinh co nghiem kep
# TH3 => delta < 0 phuong trinh co 2 nghiem phan biet

print("Giai phuong trinh bac 2 => ax^2 +bx + c = 0")
a = float(input("Nhap a => "))
b = float(input("Nhap b => "))
c = float(input("Nhap c => "))

#vs a,b,c != 0

delta = b ** 2 - 4 * a * c
if delta < 0:
    print("phuong trinh vo nghiem!")
elif delta == 0:
    print("Phuong trinh co 1 nghiem x = ", -b/(2*a))
else:
    print("Phuong trinh co 2 nghiem phan biet!")
    print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
    print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))
