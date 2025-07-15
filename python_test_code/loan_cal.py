# Get The Details From User
money_owed = float(input("How much money is still outstanding, in dollars:\n")) #100,000
int_rate = float(input("Annual Percentage Rate For The Loan:\n")) #3.00%
regular_payment = float(input("Regaular Monthly Payment in dollars:\n")) #5,000
amortization = int(input('Amortization Table For Number Of Months:\n')) #60

# Monthly Interest Rate
monthly_interest_rate = int_rate/100/12

for a in range(amortization):

    # Interest To Pay
    interest_to_pay = money_owed*monthly_interest_rate

    # Outstanding Running Balance
    money_owed = money_owed + interest_to_pay

    # Check Did The Loan Is Paid Out.
    if (money_owed - regular_payment < 0):
        print("The last Payment Is", money_owed)
        print("You Loan Is Paid Off in", a+1, "months")
        break

    # Outstanding Principal Balance
    money_owed = money_owed - regular_payment

    #print("Paid",regular_payment, "of which",interest_to_pay, "was interest")
    #print("Now I Owe", money_owed)

    print("Paid",regular_payment, "of which",interest_to_pay, "was interest", end=' ')
    print("Now I Owe", money_owed)