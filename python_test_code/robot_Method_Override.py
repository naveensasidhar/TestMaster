class Robot:
    def make_noise(self):
        print("Woof Woof!!!")

class Robot_Dog:
    def make_noise(self):
        super().make_noise()
        print("Klaa Klaa")

my_robot_dog = Robot_Dog("Jimmy")
my_robot_dog.make_noise()