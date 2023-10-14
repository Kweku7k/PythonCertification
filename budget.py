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
        newbalance = balance - amount
        print("Balance: ", balance)
        if balance >= amount:
            self.ledger.append({"amount":-abs(amount), "description":description })
            # self.balance = newbalance
            return True
        else:
            return False
        
    def transfer(self, amount, category):
        # Check to see whether transactions are feasible
        withdrawal = self.withdraw(amount, description=f"Transfer to {category.name}")
        print(withdrawal)

        deposit = category.deposit(amount, description=f"Transfer from {self.name}")
        print(deposit)

        return withdrawal
        

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False
    

    def __str__(self):
        descriptionMaxLength = 23
        lenghtOfString = len(self.name)
        asterix = int((30 - lenghtOfString)/2)
        line = f'*'*int(asterix) + self.name +'*'*int(asterix)
        line += '\n'
        total = 0
        for x in self.ledger:
            # get first descriptionMaxLength characters of the description
            # check to see if the characters are more that descriptionMaxLength
            description = x['description']
            descriptionLength = len(description)
            descriptionLengthDifference = descriptionMaxLength-descriptionLength
            descriptionSpacing = ' '*descriptionLengthDifference

            amount = x['amount']
            total += amount
            decimalAmount = "{:.2f}".format(amount)
            amountLength = len(decimalAmount)
            amountLengthDifference = 7-amountLength

            if descriptionMaxLength >= descriptionLength:
                line += description+descriptionSpacing
            else:
                line += description[:descriptionMaxLength]

            line += str(amountLengthDifference*' ')+str(decimalAmount) + '\n'
            print(line)

        line+='Total: '+"{:.2f}".format(total)
        print(line) 
            
        return str(line)
        
    
    








def create_spend_chart(categories):
    pass