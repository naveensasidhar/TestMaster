# List Inside The List aka.. container of containers.
menus = [["Dosa", "Sambar", "Coffee"],
         ["Rice", "Chicken", "Curd"],
         ["Chapathi", "Kurma", "Veggies", "Milk"]]

# print the details in list.
print("Breakfast menu:\t", menus[0])
print("Lunch Menu:\t", menus[1])
print("Dinner Menu:\t", menus[2])

# print selective details.
print(menus[0][1])

# use dictionary with keys
menu_dictionary = { "Breakfast": ["Dosa", "Sambar", "Coffee"],
                   "Lunch": ["Rice", "Chicken", "Curd"],
                   "Dinner": ["Chapathi", "Kurma", "Veggies", "Milk"] }

print("Breakfast Menu:\t", menu_dictionary["Breakfast"])
print("Lunch Menu:\t", menu_dictionary["Lunch"])
print("Dinner Menu:\t", menu_dictionary["Dinner"])

# for loop for dictionary.
# this is only going to print the keys alone.
for menu_item in menu_dictionary:
    print(menu_item)

# to get the keys and corresponsding values in a dictionary.
for name,menu in menu_dictionary.items():
    print(name, ":", menu)