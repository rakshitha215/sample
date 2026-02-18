# Initial data
balance = 10000
correct_pin = "1234"

# Function to verify PIN
def verify_pin():
    pin = input("Enter your 4-digit PIN: ")

    # Using built-in functions
    if pin.isdigit() and len(pin) == 4 and pin == correct_pin:
        print("PIN verified successfully!\n")
        return True
    else:
        print("Incorrect PIN! Access Denied.")
        return False


# Function to check balance
def check_balance():
    print("Your current balance is: Rs.{:.2f}\n".format(balance))


# Function to deposit money
def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        
        if amount <= 0:
            print("Invalid amount!\n")
        else:
            balance += amount
            print("Deposit successful!")
            print("Updated Balance: Rs.{:.2f}\n".format(balance))
    
    except ValueError:   # Built-in exception
        print("Please enter a valid number!\n")


# Function to withdraw money
def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount!\n")
        elif amount > balance:
            print("Insufficient balance!\n")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance: Rs.{:.2f}\n".format(balance))

    except ValueError:
        print("Please enter a valid number!\n")


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
            exit()   # built-in function
        else:
            print("Invalid choice! Try again.\n")


# Main Program
if verify_pin():
    atm_menu()
