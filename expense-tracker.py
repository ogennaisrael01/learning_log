import json

print("---My Expense Tracker---")
# keep track of expenses (add your expenses)
def add_expense(expenses):
    while True:
        expense_ID = input("Enter the expense id: ")
        expense_amount = float(input("Enter the expense amount: "))
        expense_category = input("Enter expense category: ")
        date = input("Enter date (DD-MM-YYYY): ")
        description = input("Description(optional): ")

        expenses.append({"Expense ID": expense_ID, "Amount": expense_amount, "Category": expense_category, "Date": date, "Description": description})
        adddinng_complete =  input("Adding completed: Y/N: ").lower()
        if adddinng_complete == "y":
            break
    print(expenses)
    print("Expenses Added Successfully")
    
#stores your expenses in a json
    filename = "expenses.json"
    with open(filename, "w") as f:
        json.dump(expenses, f)
# fetch your stored expenses from json
def fetch_expenses():
    filename = "expenses.json"
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
# Filter expense by category 
def expense_by_category(expenses):
    category = input("Enter the category to filter: ")
    filtered_category = []
    for expense in expenses:
        if category == expense["Category"]:
            filtered_category.append(expense)
            return filtered_category
#view the overall total
def overall_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    return total
    # calculate the total by category
def calculate_total_by_catogory(expenses):
    total = 0
    category_to_calculate = input("Enter the category to calculate")
    for expense in expenses:
        if category_to_calculate == expense["Category"]:
            total += expense["Amount"]
    return total



#add_expense(expenses=[])
print(fetch_expenses())
expense = fetch_expenses()
print(expense_by_category(expense))
#print(overall_total(expense))
#print(calculate_total_by_catogory(expense))
