import datetime
 
class Transaction:
    def __init__(self, type_, amount, timestamp=None, target=None):
        self.type = type_
        self.amount = amount
        self.timestamp = timestamp or datetime.datetime.now()
        self.target = target
 
    def __repr__(self):
        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        
        base = f"[{time_str}] {self.type} amount: {self.amount}"
        
        if self.target:
            return f"{base} (target: {self.target})"
        
        return base
 
class GoldAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.history = []
 
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Insufficient funds")
        else:
            self.balance += amount
            self.history.append(Transaction('deposit', amount))
 
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Insufficient funds")
        
        else:
            self.balance -= amount
            self.history.append(Transaction('withdraw', amount))
 
    def transfer_to(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

        self.history.append(Transaction('transfer', -amount, target=other.owner))
        other.history.append(Transaction('transfer', amount, target=self.owner))

    def __repr__(self):
        return f"<{self.owner}: {self.balance} gold>"
 

alice = GoldAccount("Alice")
bob   = GoldAccount("Bob")
 
alice.deposit(100)
alice.withdraw(30)
alice.transfer_to(bob, 50)
 
print(alice)          # Alice: 20 gold
print(bob)            # Bob: 50 gold
print("History Alice:", alice.history)
print("History Bob:  ", bob.history)