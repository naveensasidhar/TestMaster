#Let The Input The Number Of Expenses
expenses = []
total_sum= 0

num_expenses = int(input("Enter The Number Of Expenses To Fill In:\n"))

for actual_expense in range(num_expenses):
    expenses.append (float(input("Enter An Expense:")))

total_sum = sum(expenses)

print("You Spent Actually $", total_sum) 
print("You Spent Actually $", total_sum, sep = '')   