from Student import Student
from Chef import Chef
from ChineseChef import ChineseChef

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Brad", "CSE", 3.5, False)
student3 = Student("Lisa", "CSE", 1.5, True)

print(student2.on_honor_roll())

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()

