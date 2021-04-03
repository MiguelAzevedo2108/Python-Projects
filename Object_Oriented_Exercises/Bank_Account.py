class Account:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposit of {}$ Accepted".format(amount))

    def withdraw(self,amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")


if __name__ == '__main__':
    account = Account("Miguel",0)
    account.deposit(10)
    print(account.balance)
    account.withdraw(5)
    account.withdraw(10)