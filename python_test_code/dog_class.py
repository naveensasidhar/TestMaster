# object
class Robot_Dog:
    def __init__(self,name_value, breed_value):
        self.name = name_value
        self.breed = breed_value

# class method
    def bark(self):
        print("Woof Woof!!!")

# Main Program
my_dog = Robot_Dog("Jimmy", "ShihTzu")

print(my_dog.name)
print(my_dog.breed)
my_dog.bark()