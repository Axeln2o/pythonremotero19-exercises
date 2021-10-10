class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # getter - get field value
    def age(self):
        return self.__age

    @age.setter  # setter - sets a new field value
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            print("Please input a name!")
        else:
            self.__name = name
    @age.deleter
    def age(self):
        del self.__age



my_dog = Animal('Dog', 11)
my_dog.age = 3  # Sets age - uses setter
print(my_dog.age)  # Reads age - uses a getter

my_dog.name = "Beni"
print(my_dog.name)

del my_dog.age
print(my_dog.age) #will crash because of previously line
