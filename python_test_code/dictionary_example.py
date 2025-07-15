# Define the Dictionary.

acronyms = {"LOL": "Laugh Out Loud",
            "IDK": "I Don't know",
            "TBH": "To Be Honest",
            "NS": "Naveen Sasidharan",
            "BP": "Bipsa Purushothaman",
            "HN": "Harikesh Naveen"}

menu ={"Biriyani": "16",
       "Naan": "3"}

my_dict ={20: "Naveen",
          30: "Is Staying Last two digits of postal code",
          40: 50}

empty_dictionary ={}

# print the details
print(acronyms["LOL"])
print(acronyms["TBH"])
print(acronyms["NS"])

print(menu["Naan"])

print(my_dict[40])

print(empty_dictionary)

empty_dictionary["MON"] = "Monday"
empty_dictionary["SUN"] = "Sunday"

print(empty_dictionary["SUN"])

print(empty_dictionary)

# To Edit The value In Dictionary.
empty_dictionary["MON"] = "Day After Sunday"

print(empty_dictionary["MON"])

# delete a value from dictionary.
del empty_dictionary["MON"]

print(empty_dictionary)

# To Prevent program crashing if the key is not found in dictionary.
day_of_week = empty_dictionary.get("WED")
print(empty_dictionary)

# To check and print if the value returned is None.
if day_of_week:
    print(day_of_week)
else:
    print("Key Is Not Found")    

# To Show The Value fetched from dictionary and printed.
sentence = "IDK" + " what happened " + "TBH"   
print(sentence)
print("sentence:", sentence)

translation = acronyms.get("IDK") + " what happened " +acronyms.get("TBH")
print(translation)
print("translation:", translation)