
import sys
# i = 2
# while(i < 100):
#    j = 2
#    while(j <= (i/j)):
#       if not(i%j): break
#       j = j + 1
#    if (j > i/j) : print(i, " la so nguyen to")
#    i = i + 1
# print("done!")

# So nguyen to la tap hop cac so tu nhien chia het cho 1 va chinh no

# Nhập 1 số n bất kỳ từ bàn phím, in ra màn hình những số nguyên tố nhỏ hơn n

# print("Nhap vao mot so n")
# n = int(input("Nhap vao n: "))

# while n - 1 < n:
#    n += 1
#    print("n = ", n)
#    continue

# print("bye")


# print("Nhap")
# while True:
#   n =  int(input("nhap so: "))

#   print("so đã nhâp", n)
#   continue

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(5, int(n**(1/2)), 2): # Chỉ kiểm tra các số lẻ
        if n % i == 0:
            return False
    return True

print("Mời nhập giá trị N:")
n = input()
print('So nguyen to nho hon ', n)
for i in range(2, int(n)):
    if is_prime(i):
        print(i)