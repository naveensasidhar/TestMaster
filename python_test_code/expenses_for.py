#Let The Input Come In from User Itself
expenses = []
total_sum= 0

for actual_expense in range(5):
    expenses.append (float(input("Enter An Expense:")))

total_sum = sum(expenses)

print("You Spent Actually $", total_sum) 
print("You Spent Actually $", total_sum, sep = '')   
