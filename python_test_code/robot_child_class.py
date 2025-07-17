class Robot_Dog(Robot):

    def make_noise(self):
        print("Woof Woof!!!")

my_robot_dog = Robot_Dog("Jimmy")
my_robot_dog.walk(10)
my_robot_dog.make_noise()