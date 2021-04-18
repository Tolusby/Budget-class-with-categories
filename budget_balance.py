class Budget:
    def __init__(self, name, balance, description):
        self.name = name
        self.balance = balance
        self.description = description
        
    def show_food_budget(self):
        print('{}\n'
        ' Balance is ${}\n '
        "Descrption: {}"
        .format(self.name,  self.balance, self.description))
    def show_cloth_budget(self):
        print('{}\n'
        ' Balance is ${}\n '
        "Descrption: {}"
        .format(self.name,  self.balance, self.description))
    def show_entertainment_budget(self):
        print('{}\n'
        ' Balance is ${}\n '
        "Descrption: {}"
        .format(self.name,  self.balance, self.description))
    def show_housing_budget(self):
        print('{}\n'
        ' Balance is ${}\n '
        "Descrption: {}"
        .format(self.name,  self.balance, self.description))
    def show_savings_budget(self):
        print('{}\n'
        ' Balance is ${}\n '
        "Descrption: {}"
        .format(self.name,  self.balance, self.description))
    
food_Budget = Budget('Food budget', 30000, 'Touch am and you go starve')
food_Budget.show_food_budget()

cloth_Budget= Budget('Clothing budget', 40000, 'Make I dey soft')
cloth_Budget.show_cloth_budget()

entertainment_Budget= Budget('Entertainment', 5000, 'My no Jack fit dull')
entertainment_Budget.show_entertainment_budget()

housing_Budget = Budget('Housing',40000, 'Underbridge no soft')
housing_Budget.show_housing_budget()

other_savings_Budget = Budget('Saving', 7000, "Dangote still dey find money")
other_savings_Budget.show_savings_budget()


