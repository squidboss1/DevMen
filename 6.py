
class Student:
    def __init__(self, name, surname, sex, age):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Sex: {self.sex}")
        print(f"Age: {self.age}")

student1 = Student("Jan", "Kowalski", "Mężczyzna", "35")
student1.print_information()
