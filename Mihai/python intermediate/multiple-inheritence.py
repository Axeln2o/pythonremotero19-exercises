
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self, name, age, rate, num_of_hour):
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hour = num_of_hour

    def show_finance(self):
        return self.rate * self.num_of_hour


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hour, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hour)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate *self.num_of_hour+self.scholarship


if __name__=="__main__":
    ws=WorkingStudent("Ion",20,10,160,500)
    print(ws.show_finance())
