class Animal:
    def __init__(self, name="Rex", age=2):
        self._name = name
        self._age = age


my_dog = Animal()
print(my_dog._name)  # It will give the value of the name field of the my_dog object
