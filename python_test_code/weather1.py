# AND Condition
temperature = 75
forecast = "rainy"

if temperature < 80 and forecast != "rainy":
    print("Enjoy The Day Outside")
else:
    print("Stay Inside For The Day")    


temperature = 75
forecast = "sunny"

if temperature < 80 and forecast != "rainy":
    print("Enjoy The Day Outside")
else:
    print("Stay Inside For The Day")     


# NOT Condition
#temperature = 75
forecast = "rainy"

if not forecast == "rainy":
    print("Enjoy The Day Outside")
else:
    print("Stay Inside For The Day")      

# Boolean Condition
raining = True   
if raining:
    print("Raining Stay Inside") 

raining = False 
if not raining:
    print("Enjoy Go Outside And Enjoy")
else:
    print("It's Not A Good Day Stay Inside")    
