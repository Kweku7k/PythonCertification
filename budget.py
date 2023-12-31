import math
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
        
    
    







def getPercentatges(categories):
    array = []
    
    totalWithdrawals = 0
    for category in categories:
        withdrawals = 0
        deposits = 0
        # withdrawals/get_balance * 100?
        for l in category.ledger:
            if l['amount'] < 0:
                withdrawals += l['amount']
            else:
                deposits += l['amount']
        
        totalWithdrawals += withdrawals
        array.append({'name':category.name,'withdrawals':withdrawals})
        # withdrawals from each category over total withdrawals * 100 to get percentage

    for category in array:
        percentage = (abs(category['withdrawals']) / abs(totalWithdrawals))*100
        category['percentage'] = percentage

    return array

def rightAlign(x):
    maxLength = 3
    length = len(str(x))
    difference = maxLength - length
    rightAlignedValue = (' '*difference) + str(x)
    return rightAlignedValue


def create_spend_chart(categories):
    percentages = getPercentatges(categories)
    # print the values as a bar chart
    barChart = f''
    barChart += 'Percentage spent by category\n'
    for x in reversed(range(0, 110, 10)):
        label = rightAlign(x)
        barChart+=label+'| '
        for p in percentages: #This should preserve the order
            value = int(round(p['percentage'], -1))
            value = math.floor(p['percentage'] / 10) * 10
            if value == x or p.get('active'): #We might have to strip some values
                barChart += 'o  '
                p['active'] = True
            else:
                barChart += '   '
        barChart +='\n'
    lineBreak = ''
    lineBreak += rightAlign(' ')+' -'
    for p in percentages:
        lineBreak += '---'
        # function to check if the category is in that range
    lineBreak += '\n'
    length = len(lineBreak)
    barChart += lineBreak
    print(length)
    return barChart
    
