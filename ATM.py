# Initial data
balance = 10000
correct_pin = "1234"


# Function to verify PIN
def verify_pin():
    pin = input("Enter your 4-digit PIN: ")
    if pin == correct_pin:
        print("PIN verified successfully!\n")
        return True
    else:
        print("Incorrect PIN! Access Denied.")
        return False


# Function to check balance
def check_balance():
    global balance
    print(f"Your current balance is: Rs.{balance}\n")


# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        balance += amount
        print(f"Rs.{amount} deposited successfully.")
        print(f"Updated Balance: Rs.{balance}\n")
    else:
        print("Invalid amount!\n")


# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= 0:
        print("Invalid amount!\n")
    elif amount > balance:
        print("Insufficient balance!\n")
    else:
        balance -= amount
        print(f"Rs.{amount} withdrawn successfully.")
        print(f"Remaining Balance: Rs.{balance}\n")


# Function to display menu
def atm_menu():
    while True:
        print("====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Main Program
if verify_pin():
    atm_menu()
