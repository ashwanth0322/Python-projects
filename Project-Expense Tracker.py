#creating a Expense Tracker using Loop 
class ExpenseTracker():

    def __init__(self):
        self.expenses=[]

    def add_expense(self,amount):
       self.expenses.append(amount)

    def View_Expenses(self):
        print("Expenses :",self.expenses)

    def total_expense(self):
        total=0
        for expense in self.expenses:
            total+=expense
        print("Total Expense :",total)

    def highest_expense(self):
        try:
             print("Highest Expense :",max(self.expenses))
        except ValueError:
             print("Enter a Valid list of Expenses")



tracker=ExpenseTracker()


while True:
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Highest Expense")
        print("5. Exit")
        try:
            choice=int(input("Enter the choice: "))
            
            if choice == 1:
                amount=int(input("Enter the amount: "))
                tracker.add_expense(amount)
            
            elif choice == 2:
                tracker.View_Expenses()

            elif choice == 3:
                tracker.total_expense()

            elif choice == 4:
                tracker.highest_expense()
            
            elif choice == 5:
                print("Thank you Visiting")
                break
            
            else:
                print("Choose a Valid Choice")
        except ValueError:
            print("Please Enter a Integer")