import pyttsx3 # pip install pyttsx3( Text-to-speech library )
import json
import os 
from datetime import datetime

engine = pyttsx3.init()
DATA_FILE = "bank_data.json" # File to store user data

def speak_and_print(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Start
speak_and_print("Welcome to the Smart Banking Program!")

users = load_data()
username = input("Enter your name: ").strip().lower()

if username not in users:
    speak_and_print("New user detected. Let's create your account.")
    pin = input("Set a 4-digit PIN: ").strip()
    users[username] = {
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }
    speak_and_print("Account created successfully.")
else:
    speak_and_print("Existing user found. Please enter your PIN.")
    for attempt in range(3):
        entered_pin = input("Enter your 4-digit PIN: ").strip()
        if entered_pin == users[username]["pin"]:
            speak_and_print("Login successful!")
            break
        else:
            speak_and_print("Incorrect PIN. Try again.")
    else:
        speak_and_print("Too many wrong attempts. Exiting.")
        exit()

# Timestamp function
def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def show_balance(user_data):
    speak_and_print(f"Your current balance is ${user_data['balance']:.2f}")

def deposit(user_data):
    speak_and_print("Enter the amount to deposit:")
    try:
        amount = float(input("Amount to deposit: "))
        if amount <= 0:
            speak_and_print("Amount must be more than zero.")
            return
        user_data["balance"] += amount
        user_data["transactions"].append({
            "type": "deposit",
            "amount": amount,
            "timestamp": current_time()
        })
        speak_and_print(f"Deposited ${amount:.2f} successfully.")
    except ValueError:
        speak_and_print("Invalid input.")

def withdraw(user_data):
    speak_and_print("Enter the amount to withdraw:")
    try:
        amount = float(input("Amount to withdraw: "))
        if amount <= 0:
            speak_and_print("Amount must be more than zero.")
            return
        if amount > user_data["balance"]:
            speak_and_print("Insufficient balance.")
            return
        user_data["balance"] -= amount
        user_data["transactions"].append({
            "type": "withdraw",
            "amount": amount,
            "timestamp": current_time()
        })
        speak_and_print(f"Withdrawn ${amount:.2f} successfully.")
    except ValueError:
        speak_and_print("Invalid input.")

def show_transactions(user_data):
    if not user_data["transactions"]:
        speak_and_print("No transaction history yet.")
        return
    speak_and_print("Transaction history:")
    for i, txn in enumerate(user_data["transactions"], 1):
        speak_and_print(f"{i}. {txn['type'].capitalize()} of ${txn['amount']} on {txn['timestamp']}")

def main():
    user_data = users[username]
    is_running = True
    while is_running:
        speak_and_print("\nChoose an option:")
        print("""
        1. Show Balance
        2. Deposit Money
        3. Withdraw Money
        4. View Transaction History
        5. Exit
        """)
        engine.say("Press 1 for balance, 2 to deposit, 3 to withdraw, 4 for history, 5 to exit")
        engine.runAndWait()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            show_balance(user_data)
        elif choice == '2':
            deposit(user_data)
        elif choice == '3':
            withdraw(user_data)
        elif choice == '4':
            show_transactions(user_data)
        elif choice == '5':
            speak_and_print(f"Thank you . Goodbye !{username}")
            is_running = False
        else:
            speak_and_print("Invalid choice. Please choose between 1 to 5.")

    # Save before exiting
    save_data(users)

if __name__ == '__main__':   
    main()
# This is the main entry point for the banking program