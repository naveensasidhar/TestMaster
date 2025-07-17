# Parent Class Part
class Robot:
    def __init__(self, robot_name):
        self.name = robot_name
        self.position = [0,0]
        print("My Name Is:", self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New Position:", self.position)

# Child Class Part
class Robot_Dog(Robot):

    def make_noise(self):
        print("Woof Woof!!!")

# Main Line
my_robot_dog = Robot_Dog("Jimmy")
my_robot_dog.walk(10)
my_robot_dog.make_noise()

