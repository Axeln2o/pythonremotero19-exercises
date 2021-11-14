class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_grade(self, val_noua):
        self.grade = val_noua

    def set_age(self, val_noua):
        self.age = val_noua

    def set_name(self, val_noua):
        self.name = val_noua

student1 = Student("Alex", 29, 9.8)
student2 = Student("Mihai", 30, 9.5)
print(f" {student1.name} are {student1.get_age()}")

student1.set_age(31)
print(f" {student1.name} are {student1.get_age()}")

print(student2.get_name())
student2.set_name("Corina")
print(student2.get_name())

student2.set_grade(10)
print(student2.get_grade())
