class Expense:
    def __init__(self):
        self.Expenditure=10000
        self.Savings=5000
    def totalincome(self):
        total = self.Expenditure+self.Savings
        print('the total expenditure was',total)
E1=Expense()
E1.totalincome()