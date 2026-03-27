expenses = []  # List of dictionaries: each expense = {'category': str, 'amount': float, 'description': str}
monthly_budget = 0.0

def add_expense():
    """Add a new expense to the list."""
    category = input("Enter expense category (e.g., food, transport, entertainment, school): ").strip().lower()
    try:
        amount = float(input("Enter amount spent: $"))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    description = input("Enter a brief description: ").strip()
    
    expenses.append({
        'category': category,
        'amount': amount,
        'description': description
    })
    print(f"✅ Expense added: ${amount:.2f} for '{description}' in {category.capitalize()}")

def view_summary():
    """Display total spending, remaining budget, and category breakdown."""
    if not expenses:
        print("No expenses logged yet.")
        return
    
    total_spent = sum(exp['amount'] for exp in expenses)
    print("\n" + "="*40)
    print("📊 SPENDING SUMMARY")
    print("="*40)
    print(f"Total spent this month : ${total_spent:.2f}")
    
    if monthly_budget > 0:
        remaining = monthly_budget - total_spent
        print(f"Monthly budget set     : ${monthly_budget:.2f}")
        print(f"Remaining budget       : ${remaining:.2f}")
        
        if remaining < 0:
            print("🚨 WARNING: You have EXCEEDED your monthly budget!")
        elif remaining < monthly_budget * 0.20:
            print("⚠️  ALERT: You are within 20% of your budget limit!")
        else:
            print("✅ You are on track with your budget.")
    
    # Category breakdown using a regular dictionary (no external imports needed)
    category_totals = {}
    for exp in expenses:
        cat = exp['category']
        if cat in category_totals:
            category_totals[cat] += exp['amount']
        else:
            category_totals[cat] = exp['amount']
    
    print("\nSpending by category:")
    for cat, total in sorted(category_totals.items()):
        percentage = (total / total_spent * 100) if total_spent > 0 else 0
        print(f"  • {cat.capitalize():<15} ${total:>8.2f} ({percentage:>5.1f}%)")
    
    print("="*40)

def set_budget():
    """Set or update the monthly budget."""
    global monthly_budget
    try:
        new_budget = float(input("Enter your new monthly budget: $"))
        if new_budget <= 0:
            print("Budget must be greater than zero.")
            return
        monthly_budget = new_budget
        print(f"✅ Monthly budget updated to ${monthly_budget:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def clear_expenses():
    """Clear all logged expenses (with confirmation)."""
    confirm = input("Are you sure you want to clear ALL expenses? This cannot be undone (y/n): ").strip().lower()
    if confirm == 'y':
        expenses.clear()
        print("✅ All expenses have been cleared.")
    else:
        print("Operation cancelled.")

def main():
    """Main program loop with user menu."""
    print("🚀 Welcome to BudgetBuddy!")
    print("Your personal tool to track expenses and stay on budget.\n")
    
    while True:
        print("\n" + "-"*30)
        print("📋 MAIN MENU")
        print("-"*30)
        print("1. Add a new expense")
        print("2. View spending summary & budget status")
        print("3. Set / update monthly budget")
        print("4. Clear all expenses (reset)")
        print("5. Exit program")
        print("-"*30)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            clear_expenses()
        elif choice == '5':
            print("\nThank you for using BudgetBuddy!")
            print("Remember: Small daily tracking habits lead to big financial wins. 💰")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()