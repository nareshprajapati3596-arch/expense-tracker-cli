import sys
from datetime import datetime
import os
import json
FILES = "tracker.json"

def load_expense():
    if not os.path.exists(FILES):
        return []
    else:
        with open(FILES, "r") as f:
            return json.load(f)

def save_expense(expenses):
    with open(FILES, "w") as f:
        json.dump(expenses, f, indent= 4) 
        
def add_expense(desc, amount):
    expenses = load_expense()
    
    new_id =1
    if expenses:
        new_id = max(exp["id"] for exp in expenses) +1
        
    expense = {
        "id": new_id,
        "description": desc,
        "amount" : amount,
        "date": str(datetime.now().date())
    }
    
    expenses.append(expense)
    save_expense(expenses)
    
    print(f"Expense added successfully (ID: {new_id})") 

def list_expense():
    expenses = load_expense()
    
    if not expenses:
        print("Not found Expenses")
        return
    else:
        print("Id  Date    Description     Amount")
        for exp in expenses:
            print(f"{exp['id']}  {exp['date']}     {exp['description']}    R.{exp['amount']}")
            
def delete_expenses(expense_id):
    expenses = load_expense()
    
    new_expenses = [exp for exp in expenses if exp["id"] != expense_id ]
    
    if len(expenses) == len(new_expenses):
        print("Expense is not Found")
        return
    
    save_expense(new_expenses)
    print("Expenses was Deleted successfully")
    
def summary(month = None):
    expenses = load_expense()
    total = 0
    
    for exp in expenses:
        
        exp_month = int(exp["date"].split("-")[1])
        if month is not None and exp_month !=month:
                continue
            
        total+= exp["amount"]
        
    if month:
        print(f"Total Expenses for month {month}: {total}")
    else:
        print(f"Total Expenses: {total}")
        print("Expense:", exp["date"], "| Month:", exp_month, "| Input:", month)
        
def main():
    args = sys.argv
    
    if len(args) <2:
        print("No command Given")
        return
    
    command = args[1]
    
    if command == "add":
        if len(args) <4:
            print("Usage: Add <Descroption> <amount>")
            return
        desc = args[2]
        amount = float(args[3])
        add_expense(desc, amount)
        
    elif command == "list":
        list_expense()
    
    elif command == "delete":
        delete_expenses(args[2])
        
    elif command == "summary":
        if len(args) >2:
            summary(int(args[2]))
        
        else:
            summary()
        
    else:
        print("Unknown command")
    

if __name__  == "__main__":
    main()
    