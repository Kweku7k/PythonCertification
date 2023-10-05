class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
        
    def deposit(self, amount, description=""):
        print("Depositing: ",amount)
        self.ledger.append({"amount":amount, "description":description })

    def get_balance(self):
        total = 0
        # calculate the balance based on the withdrawals and deposits in ledger
        for l in self.ledger:
            print("Adding ", l["amount"])
            total += l["amount"]
            print(total)
        return total

    def withdraw(self, amount, description = ""):
        print("Withdrawing: ",amount)

        # check available funds first
        balance =  self.get_balance()
        print("Balance: ", balance)
        if balance >= amount:
            self.ledger.append({"amount":-abs(amount), "description":description })
            return True
        else:
            return False
        
    def transfer(self, amount, category):
        withdrawal = self.withdraw(amount, description=f"Transfer to {category.name}")
        print(withdrawal)
        deposit = self.deposit(amount, description=f"Transfer from {self.name}")
        if withdrawal == True and deposit == True:
            return False
        else:
            return True

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
        
    
    








def create_spend_chart(categories):
    pass