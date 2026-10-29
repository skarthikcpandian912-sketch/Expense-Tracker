import csv

# Store all expenses
expenses = []


# Function 1: Add Expense
def add_expense():
    category = input("Enter category: ").strip()

    # Validate category
    if category == "":
        print("Category cannot be empty!")
        return

    # Handle invalid amount
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    # Validate amount
    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    expense = {"category": category, "amount": amount}

    expenses.append(expense)

    print("Expense added successfully!")


# Function 2: View Expenses
def view_expenses():
    for expense in expenses:
        print("Category:", expense["category"], "| Amount:", expense["amount"])


# Function 3: Calculate Total
def calculate_total():
    total = sum(expense["amount"] for expense in expenses)

    print("Total Expenses:", total)


# Function 4: Category Summary
def category_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("Category Summary:", summary)


# Function 5: Save Expenses
def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Category", "Amount"])

        for expense in expenses:
            writer.writerow([expense["category"], expense["amount"]])

    print("Expenses saved successfully!")


# Function 6: Load Expenses
def load_expenses():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(
                    {"category": row["Category"], "amount": float(row["Amount"])}
                )

        print("Expenses loaded successfully!")

    except FileNotFoundError:
        print("No previous expenses found. Starting fresh.")


# Function 7: Main Menu
def main():
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")


# Execute functions in the order we studied
load_expenses()

add_expense()

save_expenses()

view_expenses()

calculate_total()

category_summary()

main()
