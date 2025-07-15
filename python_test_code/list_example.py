# List Creation
acronyms =[]

# add items to List
acronyms.append("LOL")
acronyms.append("IDK")
acronyms.append("TBD")

print(acronyms)

new_list = ["MON", "TUE", "WED"]

#append to list
new_list.append("THU")
new_list.append("FRI")
new_list.append("SAT")
new_list.append("SUN")

print(new_list)

# To remove from list
new_list.remove("SUN")
del new_list[5]

print(new_list)

# To check Values In List And respond.
#value_list = ["A", "B", "C", "D"]
input_value = input("Enter A Alphabet Between A to Z - \n")
print(input_value)
if input_value in ["A", "B", "C", "D"]:
    print("Value Is In List")
else:
    print("Values Is Not There In List")

# To check Values In List And respond - From Defined List.
value1_list = ["N", "A", "V", "Z"]
input1_value = input("Enter A Alphabet Between A to Z - \n")
print(input1_value)
if input1_value in value1_list:
    print("Value Is In New List")
else:
    print("Values Is Not There In New List")

    