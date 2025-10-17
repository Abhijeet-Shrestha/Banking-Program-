# Banking-Program


# 🏦 Smart Banking Program (Voice Assisted)

A simple **voice-enabled banking system** built in Python using `pyttsx3` for text-to-speech and `json` for data storage.  
This project allows users to **create accounts, deposit or withdraw money, check balances**, and **view transaction history** — all with voice feedback.

---

##  Features

 **Text-to-Speech Support**  
Uses `pyttsx3` to speak all messages and menu options aloud.  

 **Account Creation & Login System**  
Each user has a unique name and a secure 4-digit PIN for authentication.  

 **Deposit & Withdraw Money**  
Handles all basic banking operations with proper validation.  

 **Transaction History**  
Stores all deposits and withdrawals with timestamps.  

 **Persistent Data Storage**  
All data (users, balances, transactions) is saved in a local JSON file (`bank_data.json`).

---

##  How It Works

1. When you run the program:
   - It checks if a user already exists in `bank_data.json`.
   - If not, it creates a new account and asks you to set a 4-digit PIN.
2. After logging in, you can:
   - Check your balance  
   - Deposit money  
   - Withdraw money  
   - View your transaction history
3. All changes are automatically saved when you exit.

---

##  Menu Options

| Option | Description |
|---------|--------------|
| 1 | Show Current Balance |
| 2 | Deposit Money |
| 3 | Withdraw Money |
| 4 | View Transaction History |
| 5 | Exit Program |

---

##  Requirements

Make sure you have Python installed (>=3.7).  
Then install the required library:

```bash
pip install pyttsx3

