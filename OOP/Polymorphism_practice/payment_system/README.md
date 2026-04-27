# 💳 Payment System — Polymorphism Practice

A Python-based Object-Oriented Programming (OOP) project demonstrating **Polymorphism, Inheritance, Magic Methods, and Exception Handling** using a real-world payment processing system.

---

## 🚀 Project Overview

This project simulates a payment system that supports multiple payment methods:

* Credit Card
* UPI
* Net Banking

Each payment type shares a common structure but behaves differently, showcasing the power of **polymorphism**.

---

## 🧠 Key Concepts Used

* **Polymorphism** → Same method, different behavior (`process()`, `receipt()`)
* **Inheritance** → Base class `Payment`, extended by child classes
* **Method Overriding** → Each payment type defines its own logic
* **Magic Methods** → `__str__`, `__gt__`, `__eq__`
* **Exception Handling** → Custom exceptions for validation errors
* **JSON Handling** → Save payment data into a file

---

## 🏗️ Project Structure

```
polymorphism-practice/
│
├── payment_system.py     # Main Python file
├── Payments.json         # Auto-generated JSON file (after running)
└── README.md             # Project documentation
```

---

## 💳 Supported Payment Types

### 1. Credit Card

* Validates 16-digit card number
* Masks card details in receipt

### 2. UPI

* Validates presence of `@`
* Example: `user@upi`

### 3. Net Banking

* Validates account number (10–12 digits)
* Masks account number in receipt

---

## ⚙️ How It Works

1. Create payment objects
2. Add them to `PaymentProcessor`
3. System validates and processes each payment
4. Generates receipts
5. Saves all transactions to JSON file

---

## ▶️ How to Run

### Step 1: Navigate to project folder

```bash
cd polymorphism-practice
```

### Step 2: Run the program

```bash
python payment_system.py
```

---

## 📄 Sample Output

```
Credit Card Payment of 5000 processed successfully!
UPI Payment of 1500 processed successfully
NetBanking Payment of 3000 processed!

── All Receipts ──
[CreditCard] Raj Kumar | **** **** **** 3456 | 5000 | 2026-04-27
[UPI] raj@upi | 1500 | 2026-04-27
[NetBanking] SBI | XXXXXX8901 | 3000 | 2026-04-27
```

---

## 📁 JSON Output

After execution, a file `Payments.json` is created:

```json
[
    {
        "type": "CreditCard",
        "amount": 5000,
        "currency": "INR",
        "date": "2026-04-27 10:30",
        "holder_name": "Raj Kumar",
        "card_last4": "3456"
    }
]
```

---

## 🔥 Key Features

* Clean OOP design
* Secure data masking
* Custom exception handling
* Extendable architecture
* Real-world use case simulation

---

## 📌 Future Improvements

* Add **Crypto payments**
* Add **Refund functionality**
* Build **CLI menu system**
* Convert into **Flask API + React frontend**

---

## 👨‍💻 Author

**Mayur Biradar**
Aspiring Software Developer | MERN Stack Learner

---

## ⭐ Conclusion

This project is a strong demonstration of **core OOP principles in Python**, especially **polymorphism**, using a practical and scalable design.

---
