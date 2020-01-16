
#Hàm này có tác dụng chuyển đổi chuỗi về dạng in thường.
string = "Nguyen Ngoc Thang"
print(string.lower())

#Hàm này có tác dụng chuyển đổi chuỗi sang dạng in hoa.
string = "Nguyen Ngoc Thang"
print(string.upper())

#Chỗi là ký tự số
#isdigit()
#isnumeric()

string = '12051996'
print(string.isnumeric())
print(string.isdigit())

#Hàm này có tác dụng tìm kiếm và thay thế chuỗi tìm được bằng chuỗi mới.
#string.replace(old,new,max)
string = "Thang"
print(string.replace('g', 'h'))

#Hàm này có tác dụng chuyển đổi chuỗi sang kiểu title
string = "nguyen ngoc thang"
print(string.title())


#Hàm này có tác dụng tác chuỗi thành mảng bởi các char.
#string.split(char, max)

string = "nguyen ngoc thang"
print(string.split())

string = "nguyen ngoc thang"
print(string.split('a'))


string = "nguyen ngoc thang"
print(string.split(' ', 1))

string = "nguyen ngoc thang"
print(string.split(' ', 4)) #n

