import json
from datetime import datetime

# base class

class Payment:
    def __init__(self,amount, currency="INR"):
        self.amount = amount
        self.currency = currency
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def process(self):
        pass                      # Override in child
    
    def validate(self):
        pass                       # Override in child
    
    def receipt(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} | {self.currency} {self.amount}"
    
    def __gt__(self, other):
        return self.amount > other.amount
    
    def __eq__(self, other):
        return self.amount == other.amount
    
    def to_dict(self):
        return {
            "type" : self.__class__.__name__,
            "amount" : self.amount,
            "currency" : self.currency,
            "date" : self.date
        }
        
# ___ CHILD CLASSES _____

class CreditCard(Payment):
    def __init__(self, amount, card_number, holder_name):
        super().__init__(amount)
        self.card_number = card_number
        self.holder_name = holder_name
        
    def validate(self):
        if len(self.card_number) != 16 or not self.card_number.isdigit():
            raise InvalidPaymentError("Invalid Card Number")
        
    def process(self):
        self.validate()
        print(f"Credit card Payment of {self.amount} prcessed successfully! ")
        
    def receipt(self):
        masked = "**** **** **** " + self.card_number[-4:]
        print(f"[CreditCard] {self.holder_name} | {masked} | {self.amount} | {self.date}")
        
    def to_dict(self):
        d = super().to_dict()
        d["holder_name"] = self.holder_name
        d["card_last4"] = self.card_number[-4:]
        return d

class UPI(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id
        
    def validate(self):
        if "@" not in self.upi_id:
            raise InvalidPaymentError("Invalid UPI ID")
        
    def process(self):
        self.validate()
        print(f"Upi Payment of {self.amount} processed successfully")
        
    def receipt(self):
        print (f"[UPI] {self.upi_id} | {self.amount} | {self.date}")
        
    def to_dict(self):
        d = super().to_dict()
        d["upi_id"] = self.upi_id
        return d
    
class NetBanking(Payment):
    def __init__(self, amount, bank_name, account_number):
        super().__init__(amount)
        self.bank_name = bank_name
        self.account_number = account_number

    def validate(self):
        if not (10 <= len(self.account_number) <= 12) or not self.account_number.isdigit():
            raise InvalidPaymentError("Invalid Account Number")

    def process(self):
        self.validate()
        print(f"NetBanking Payment of {self.amount} processed!")

    def receipt(self):
        masked = "XXXXXX" + self.account_number[-4:]
        print(f"[NetBanking] {self.bank_name} | {masked} | {self.amount} | {self.date}")

    def to_dict(self):
        d = super().to_dict()
        d["bank_name"] = self.bank_name
        d["account_last4"] = self.account_number[-4:]
        return d
    
# ____ CUSTOM EXCEPTIONS ___ 

class PaymentError(Exception):
    pass

class InsufficientFundsError(PaymentError):
    pass

class InvalidPaymentError(PaymentError):
    pass

#_____ PAYMENT PROCESSOR _____

class PaymentProcessor:
    def __init__(self):
        self.payments = []
        self.total = 0
        
    def add_payment(self, Payment):
        try:
            Payment.validate()
            Payment.process()
            self.payments.append(Payment)
            self.total += Payment.amount
        except PaymentError as e:
            print(f"Error: {e}")
            
    def largest_payment(self):
        if not self.payments:
            return None
        return max(self.payments)
    
    def total_amount(self):
        return self.total
    
    def save_to_json(self, filename="Payments.json"):
        data = [p.to_dict() for p in self.payments]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("saved to JSON!")
        
    def summary(self):
        print("\n -- SUMMARY --")
        for p in self.payments:
            p.receipt()
            
# ____ MAIN _____

if __name__ == "__main__":
    processor = PaymentProcessor()
    
    p1 = CreditCard(5000, "1234567890123456", "Raj Kumar")
    p2 = UPI(1500, "raj@upi")
    p3 = NetBanking(3000, "SBI", "12345678901")
    
    processor.add_payment(p1)
    processor.add_payment(p2)
    processor.add_payment(p3)
    
    print("\n -- Processing All Payments --")
    for p in [p1, p2, p3]:
        p.process()
        
    print("\n── All Receipts ──")
    for p in [p1, p2, p3]:
        p.receipt()

    print("\n── Magic Methods ──")
    print(p1 > p2)
    print(p1 == p3)
    print(p1)

    processor.summary()
    processor.save_to_json()

    print(f"\nTotal: {processor.total_amount()}")
    print(f"Largest: {processor.largest_payment()}")
