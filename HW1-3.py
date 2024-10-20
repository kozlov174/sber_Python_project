# Так выглядит класс студента и его функци до модификации
# class Student()
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def introduce(self):
#         print("Student " + self.name + " is " + self.age + " years old and study at" + self.grade + " grade" )

#Класс студента после модификации
class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.__age = age
        self.__grade = grade
    def age(self):
        return self.__age
    def grade(self):
        return self.__grade

if __name__ == '__main__':
    student = Student('Ivan', 21, 4)
    print(student.name)
    print(student.age())
    print(student.grade())





