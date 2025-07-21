acronyms = {"LOL": "laugh out loud",
            "IDK": "I don;t know",
            "TBH": "to be honest"}

# try exception block, will catch the exception and program continue running.
try:
    definition = acronyms["NAV"]
    print("Definition of", acronyms, "is" ,definition)
except:
    print("The key", acronyms, "doesn't exist")
finally:
    print("The acronyms we have defined are:")
    for acronym in acronyms:
        print(acronym)    

print("The Program Continuees!!!")

try:
    definition = acronyms["LOL"]
    print("Definition of", acronyms, "is" ,definition)
except:
    print("The key", acronyms, "doesn't exist")

print("The Program Keeps Going On !!!")

