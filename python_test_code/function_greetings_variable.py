# In this example the variable is not defined inside the function.
# function definition
def greeting():
    print("Hello", name)
#Main Program
# Here the variable "name" is defined as part of main line and the same is exposed to definistion defined in this module.
name = input("Enter Your Name:\n")
greeting()

name2 = input("Enter Another Name:\n")
name = name2
greeting()