class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


    def myfunc(self):
        print("myfunc =>", self.age)



#person = Person('thang', 20, 'Hanoi')
# print(person.name)
# print(person.age)
#person.myfunc()


class Student(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)
        self.sex = "nam"

    def welcome(self):
        print("welcome", self.address, self.sex)

x = Student("thang", 20, "address")
# x.myfunc()
# print(x.sex)
x.welcome()

