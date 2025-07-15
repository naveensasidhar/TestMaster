## To Test The Initial Program.
print("This Is my First Code ...!!!")

## To allow the comments to feed to multiple lines.
print("""To Test Multi - line comments 
Line-1,
Line-2""")

## Variables
firstName = 'Naveen'
lastName = 'Sasidharan'
print(f'First Name - {firstName}')
print(f'Last Name - {lastName}')
fullName = firstName + " " + lastName
print(f'Full Name - {firstName},{lastName}')
print(f'Full Name - {fullName}')

## Appending Operations
string1 ='Harikesh'
string1 += ' Naveen'
print(string1)

## Join() For Multiple List
string2 = ['Harikesh', ' Naveen', ' Is A Good', ' Boy']
result = "".join(string2)
print(result)

## f Formatting
name = 'Harikesh Naveen'
age = 11
result = f'My name Is {name} and I am {age} years old.'
print(result)

print(f'My name Is {name} and I am {age} years old.')

## %Operator - for formatting and concatenation
result = '%s %s' % (firstName, lastName)
print(result)

## List concatenation
list1 = [1,2,3,4,5]
list2 =[6,7,8,9,10]
result = list1 + list2
print(result)

## Extend
list1.extend(list2)
print(list1)

## List Comprehension
result =[x for sublist in [list1, list2] for x in sublist]
print(result)

## Type Check
typeString = str(10)
typeInteger = int(1)
typeFloat = float(3.22)
typeComplex =complex(3+1j)
typeBoolean = bool(0)
#typeNone = NoneType() 

print(typeString)
print(typeInteger)
print(typeFloat)
print(typeComplex)
print(typeBoolean)
print(type(firstName))
print(type(age))
print(type(list1))
print(type(typeComplex))

## Variable As Global & Inside The Function.
globalVariable = 'This Is A Global Variable'

def firstfunc():
    global newVariable
    globalVariable = 'This Variable Is Inside The Function Assigned'
    newVariable = 'Global Variable Defined Exclusively Inside The Function'
    print('Output Inside The Function - ' + globalVariable)

firstfunc()

print(f'Output Outside The Function - {globalVariable}')
print(f'Printing Of Global Variable - {newVariable}')

# Built in function - random, to get a number between 1 & 100
import random
print(random.randrange(1,100))