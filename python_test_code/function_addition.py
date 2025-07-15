#function defention
def addition(a,b):
    return a+b

# Main Program Is Moved as a Main function
def main():
    number_1 = float(input("Enter The First Number:\n"))
    number_2 = float(input("Enter The Second Number:\n"))

    # Invoking the function
    result = addition(number_1,number_2)
    print("Sum Of Two Numbers:", result)

main()