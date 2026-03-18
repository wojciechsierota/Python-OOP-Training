class Result:
    def __init__(self, message, value=None):
        self.isSuccess = None
        self.message = message
        self.value = value 

    def __str__(self):
        status = "SUCCESS" if self.isSuccess else "ERROR"
        return f"[{status}] {self.message}: {self.value}"


class OK(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = True


class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.isSuccess = False


class BankAccount:
    def __init__(self, start_balance=0):
        self._balance = 0
        self.balance = start_balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_value):
        if new_value < 0:
            print("LOG: Blocked attempt to set a negative balance!")
        else:
            self._balance = new_value
        
    def deposit_money(self, money_to_deposit):
        if money_to_deposit > 0:
            self.balance += money_to_deposit
            return OK("Money deposited successfully", money_to_deposit)
        return Error("Deposit amount must be positive", money_to_deposit)
    
    def withdraw_money(self, money_to_withdraw):
        if self.balance >= money_to_withdraw:
            self.balance -= money_to_withdraw
            return OK("Money withdrawn successfully", money_to_withdraw)
        else:
            return Error("Insufficient funds", self.balance)
        
    def show_my_balance(self):
        return OK("Current account balance", self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimum_balance=1000):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def withdraw_money(self, money_to_withdraw):
        if (self.balance - money_to_withdraw >= self.minimum_balance):
            return super().withdraw_money(money_to_withdraw)
        else:
           return Error("Minimum balance threshold exceeded", self.minimum_balance)


# --- TEST SCENARIO ---
account = MinimumBalanceAccount(1500, 1000)
print(account.deposit_money(500))
print(account.withdraw_money(1200))
print(account.withdraw_money(200))
print(account.show_my_balance())