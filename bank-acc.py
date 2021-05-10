class User:		# declare a class and give it name User
    name=""
    email=""
    account_balance=0
    def __init__(self,name,email,balance):
        self.name = name
        self.email = email
        self.account_balance =balance
    def deposit(self,amount):
        self.account_balance+=amount
        print("success, you added",amount,". Your current Balance is",self.account_balance)
    def withdrawal(self, amount):
        if amount<=self.account_balance:
            self.account_balance -= amount
        else:
            print("not enough")
    def display_user_balance(self):
        print("mr.",self.name,"has a balance of",self.account_balance)
#end of class
drake = User("drake","drake@gmail.com",1000)
josh = User("josh", "josh@gmail.com",1100)
megan = User("megan","megan@gmail.com",1300)
drake.deposit(300)
drake.deposit(200)
drake.deposit(500)
drake.withdrawal(900)