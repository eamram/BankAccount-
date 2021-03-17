class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.transaction = []

    def show(self):
        # TODO: add format
        print(self.owner, self.balance)

    def deposit(self, amount, description, currency):
        if amount < 0:
            print("you should enter positive number")
            return "your transaction wasn't recorded"
        self.transaction.append(Transaction(amount, description, currency))
        return "your transaction was recorded"

    def withdrawal(self, amount, description, currency):
        if amount < 0:
            print("you should enter positive number")
            return "your transaction wasn't recorded"
        self.transaction.append(Transaction(-amount, description, currency))
        return "your transaction was recorded"

    def showTransactions(self, limit):
        print(list(reversed(self.transaction[-limit:])))


class Transaction:
    def __init__(self, amount, description, currency):
        self.amount = amount
        self.description = description
        self.currency = currency

    def __repr__(self):
        # TODO: reformat
        return f'{self.amount}{self.description}{self.currency}'


Account1 = BankAccount(owner='Eyal')

Account1.show()
Account1.deposit(4, "give1", "ILS")
Account1.withdrawal(4, "took", "ILS")
Account1.deposit(5, "give2", "ILS")

Account1.showTransactions(2)
