'''Object Orientated Programing in Python'''

print(type("hello"))
''' "String"- ul este si el o clasa. Textul din interiorul stringului este defapt "obiectul" clasei'''
''' "type" este o functie - nu stiam'''
''' Dupa ce dam run, ne da mesajul "class'string'" '''

x = 1
print(type(x))
''' Vom observa ca dupa ce dam run, ne da un mesaj, "class 'int'", asta pt ca x = 1 este un integer'''


def hello():
    print("hello")


print(type(hello))
''' Vom observa ca dupa ce dam run, ne da mesajul "class 'function'", asta pentru ca mai sus am scris 'def' '''

string = "hello"
print(string.upper())
'''#.upper este o metoda; este o metoda aplicata obiectului din string. in cazul de fata este o metoda de 
                          a modifica din litere mici in litere mari obiectul ce se afla in string'''






class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 10
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
            if len(self.students) < self.max_students:
                self.students.append(student)
                return True
            return False
    def get_average_grade(self):
            value = 0
            for student in self.students:
                value += student.get_grade()
            return value / len(self.students)
s1 = Student("Tim", 19, 10)
s2 = Student("Benny", 19, 8)
s3 = Student("Jill", 19, 6)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_average_grade())
