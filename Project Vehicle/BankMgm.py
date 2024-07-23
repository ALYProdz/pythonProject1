

class Bank:
    """Bank"""
    def __init__(self, full_name, account_number, Balance, ):
        """n"""
        self.fullname = full_name
        self.account_number = account_number
        self.Balance = Balance

    def Deposit(self, Amount):
        if Amount>0:
            self.Balance +=Amount
    def get_name(self):
        print("Account name : ",self.fullname)
    def get_balance(self):
        print("Balance : ",self.Balance)

    def with_draw(self, amount):
        self.Balance -= amount

    def account_info(self):
        print("Account owner : ", self.fullname)
        print("Account number : ", self.account_number)
        print("Account Balance : ", self.Balance)

client_1 = Bank("Wednika", "123-343-5676", 2343)
client_2 = Bank("Jimmy Kerry", "234-345-5676", 345)

#Display the information about the account
print(client_1.account_info())
#Let's put 1000 in our account
client_1.Deposit(1000)
#Display the new output
print(client_1.account_info())

#Let's withdraw 300

client_1.with_draw(300)
#display new output
print(client_1.account_info())

client_2.get_balance()
client_2.account_info()
client_2.Deposit(12400)
client_2.account_info()
client_2.get_name()



