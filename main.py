class BankAccount:
    """
        We want the user to be able to crate a new bank account
        with account number, account holder name and initial balance
    """
    balance = 0
    def __init__(self, acc_number,acc_name, initial_balance=500):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = initial_balance
        BankAccount.balance += self.balance

    def deposit(self, amount):
        self.balance += amount
        BankAccount.balance += amount
        return f"Hello, {self.acc_name}, you have successfully deposited {amount} and your balance is {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            BankAccount.balance -= amount
            return f"Hello, {self.acc_name}, you have successfully withdrawm Ksh {amount}. Your balance is {self.balance}"
        else:
            return "Insufficient funds"

    @classmethod
    def total_balance(cls):
        return cls.balance



joel = BankAccount("1234", "Joel Nyongesa", 1000)
joel.deposit(10000)
print(BankAccount.balance)
# print(joel.deposit(1000))
# print(joel.withdraw(1000))
# print(joel.get_balance())
