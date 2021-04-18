
def init():
    print('Welcome to Savermo \n')
    print ('Your favourite savings app \n')
    selectedOption = int(input('  What will you like to do (1) Withdrawal (2) Deposite (3) Tranfer (4) Check Balances (5) Make a complaint  (6) Exit \n'))
    if selectedOption == 1:
        withdrawl(self)
    elif(selectedOption == 2):
      deposite(self)
    
    elif(selectedOption == 3):
      transfer(self)
    elif(selectedOption == 4):
      get_balance(self)
        
    elif(selectedOption == 5):
      complaint(self)
    
    elif(selectedOption == 6):
            exit()
    else:
        print('You have selescted an invalid option')
        
def complaint():
    complaint= input('Write your complaints below \n')
    print ('Thank you for your feedback')


class Budget:
    
    def __init__(self,category,amount):
        self.category = category
        self.amount = amount 
        self.wallet = list()
    def deposit( self,amount,description=""):
        self.wallet.append({'amount': amount, 'description': description})
    
    def withdrawal(self,amount,description=""):
        if (self,avaliable_funds(amount)):
            self.wallet.append({'amount': -amount, 'description': description})
            return True
        return False 
    def get_balance(self):
        total_balance = 0
        for item in self.wallet:
            total_balance += item('amount')
        return total_balance
    def transfer(self,amount,category):
        if(self.check_funds(amount)):
            self.withdrawal(amount,'has been transfered to '+ category.name)
            category.deposite(amount,'has been transfered from' +self.name)
            return True
        return False
    def check_funds(self,amount):
        if(self.get_balance() >= amount):
            return True
        return False



cat_1= Budget('Food',0)
cat_2= Budget('Clothing', 0)
cat_3 = Budget('Entertainment',0)
cat_4 =Budget('Other savings',0)





