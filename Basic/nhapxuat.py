#value = input("Nhập từ bàn phím => ")
#print("giá trị nhập từ bàn phím => ", value)


#nhập từ bàn phím vào một số rồi in ra số đó

# number = int(input("Nhập vào một số =>"))


# if isinstance(number, int):
#     print("số vừa nhâp =>", number)
# else:
#     print("nhập lại")
        

# while number < 10:




#     number += 1
#     if isinstance(number, int):
#         print("Số nhập vào từ bàn phím =>", number)
#     else:
#         print("Xin mời nhập lại")
#         continue


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


#nhập vào một số , nếu không phải số thì nhập lại

#number  = int(input("nhập vào một số => "))
#kiểm tra có phải là số hay không
# if(number.isnumeric()):
#     print("là số => ", number)
# else:
#     print("không phải số")


#List
lists = ["a","b","c"]
number = [12, 114, 16]


# for list in lists:
#     print("item of list", list)
 

# for a in number:
#     if(a == 12):
#         continue

#     print("item number ", a)

# for a in number:
#     if(a == 12):
#         print("item number ", a)  
#         break
#     print("item number ", a)   

    
#function
# def functionA(string):
#     print("my name: ", string)

# def function_1(**pars):
#   print("His last name is " + pars["lname"])

# function_1(fname = "Tobias", lname = "Refsnes")

x = lambda a : a + 10
print(x(5))
