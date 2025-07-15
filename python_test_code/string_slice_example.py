# To Get The Elements Of The basestring
string = 'Naveen Sasidharan'
stringWithBlanks = 'NaVeeN SasidharaN!!   '
age = 40
price = 121
CheckVariable = 'test for string validation.'
print(string[0])
print(string[1])
print(string[-1])
print(string[-2])

#To Loop Through string
for x in "Naveen Sasidharan":
    print(x)
    
# To Get Length Of A String
print(len(string))

# To Check For Existence In string
actualText = 'The Best Way To Reach Union Station Is Taking Go Transit'
print("Reach" in actualText)
print("union" in actualText)
if "Reach" in actualText:
    print("Yes, 'Reach' is found in string")
if "union" not in actualText:
    print("Yes, 'union' is not found in string")

# slicing Or sub string operation
print(string[3:8])
print(string[0:2])
print(string[9:]) 
print(string[-5:-2])

#string modification - upper/lower/remove whitespace
print(string.upper())
print(string.lower())
print(stringWithBlanks.strip())

# string manipulation - Replace/Split
print(string.replace("N", "B"))
print(string.replace("n", "Z"))
print(string.split(" "))
print(stringWithBlanks.split(" "))

# Concatenation
Concatenation = string + ' ' + stringWithBlanks
print(Concatenation)

# Format String - F strings
print(f'{string} Is {age} Years Old.')
print(f'The Price For Pedal Fan Is {price} dollars')
print(f'The Price For Pedal Fan Is {price:.2f} dollars')
print(f'The Answer For 10 x 5 Is {10 * 5}')

# Escape Character Use - \
print(f"To Test The Escape Character - \Today's\ cost is Very High For Gas.")

# capitalize classmethod - Converts the first character to upper case
print(CheckVariable.capitalize())

# casefold classmethod - Converts string Into lower case (This is more powerful than lower built-in function)
print(actualText.casefold())

# center classmethod - We can position The String In Screen/Output.
print(string.center(30))
print(string.center(30,"N"))

# count classmethod - Returns Number of time a specified value occur in string.
print(string.count("a"))
print(string.count("a",1,14))

# encode classmethod - Returns encoded version of the string.
encodedString = 'Value Having Ståle.'
print(encodedString.encode())
print(encodedString.encode(encoding="ascii",errors="replace"))
print(encodedString.encode(encoding="ascii",errors="ignore"))
