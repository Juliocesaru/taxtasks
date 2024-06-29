import random
import string
import datetime

# Dummy database to store user and account information
user_database = {}
account_database = {}
user_count = 0

# Function to generate user ID like BCB00000, BCB00001, etc.
def generate_user_id():
    global user_count
    user_id = f"BCB{user_count:05}"
    user_count += 1
    return user_id

# Function to send Welcome Email
def send_welcome_email(first_name, last_name, email):
    print(f"Sending Welcome Email to {first_name} {last_name} at {email}")
    # Placeholder for actual email sending logic

# Function to create a new checking or saving account
def create_account():
    global user_database, account_database
    
    print("Choose an account type:")
    print("1. Create a checking account")
    print("2. Create a saving account")
    account_type = int(input("Enter your choice (1 or 2): "))
    
    if account_type not in [1, 2]:
        print("Invalid choice. Please try again.")
        return
    
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    
    # Generate user ID
    user_id = generate_user_id()
    
    # Save user information
    user_database[user_id] = {
        'first_name': first_name,
        'last_name': last_name,
        'dob': dob,
        'email': f"{first_name.lower()}.{last_name.lower()}@beautifulcanadabank.com"  # Dummy email generation
    }
    
    # Generate account number
    account_number = ''.join(random.choices(string.digits, k=10))
    
    # Save account information
    account_database[account_number] = {
        'user_id': user_id,
        'account_type': 'Checking' if account_type == 1 else 'Saving',
        'balance': 0,
        'withdraw_limit': 1000
    }
    
    # Send Welcome Email
    send_welcome_email(first_name, last_name, user_database[user_id]['email'])
    
    print(f"Congratulations {first_name} {last_name}! Your account has been created successfully.")
    print(f"Your {account_database[account_number]['account_type']} account number is: {account_number}")
    print("")

# Function to deposit money into an account
def deposit_money():
    account_number = input("Enter your account number: ")
    amount = int(input("Enter the amount to deposit (CAD): "))
    
    if account_number in account_database:
        account_database[account_number]['balance'] += amount
        print(f"Successfully deposited {amount} CAD into account {account_number}.")
        print(f"New balance: {account_database[account_number]['balance']} CAD")
    else:
        print("Invalid account number. Please try again.")

# Function to withdraw money from an account
def withdraw_money():
    account_number = input("Enter your account number: ")
    amount = int(input("Enter the amount to withdraw (CAD): "))
    
    if account_number in account_database:
        if amount > account_database[account_number]['withdraw_limit']:
            print("Withdrawal amount exceeds current limit.")
            increase_limit = input("Do you want to increase the Withdraw limit? (yes/no): ").lower()
            if increase_limit == 'yes':
                new_limit = int(input("Enter the new maximum limit (up to 5000 CAD): "))
                account_database[account_number]['withdraw_limit'] = min(new_limit, 5000)
                print(f"Withdrawal limit updated to {account_database[account_number]['withdraw_limit']} CAD.")
            else:
                print("Withdrawal limit not changed.")
                return
        
        if amount <= account_database[account_number]['balance']:
            account_database[account_number]['balance'] -= amount
            print(f"Withdrawn {amount} CAD from account {account_number}.")
            print(f"New balance: {account_database[account_number]['balance']} CAD")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid account number. Please try again.")

# Function to remove ATM card
def remove_atm_card():
    account_number = input("Enter your account number: ")
    
    if account_number in account_database:
        del account_database[account_number]
        print(f"Account {account_number} deleted successfully.")
    else:
        print("Invalid account number. Please try again.")

# Main menu loop
def main_menu():
    print("Welcome to Beautiful Canada Bank Management System")
    while True:
        print("")
        print("Choose an option:")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Remove ATM card")
        print("5. Exit")
        
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            remove_atm_card()
        elif choice == 5:
            print("Thank you for using Beautiful Canada Bank Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Execute main menu
if __name__ == "__main__":
    main_menu()
