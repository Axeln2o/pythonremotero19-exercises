class Animal:
    def __init__(self, name="Rex", age=2):
        self.__name = name
        self.__age = age

    def print_details(self):
        print(f" Name: {self.__name}, Age: {self.__age}")


my_dog = Animal()
my_dog.print_details()
