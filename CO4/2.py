class ac:
    def __init__(self):
        self.name=str(input("Enter The Name:\n"))
        self.no=int(input("Enter Account Number:\n"))
        while True:
            self.type=int(input("\n1.Savings\n2.Current\nPlease Select a Account Type:\n"))
            if self.type==1:
                print("Savings Account")
                break
            elif self.type==2:
                print("Current Account")
                break
            else:
                print("Please Select a Valid Account Type")
        self.balance=0
    def depo(self):
        amount=int(input("Enter The Amount To Deposit:\n"))
        self.balance+=amount
    def withdraw(self):
        amount=int(input("Enter The Amount To Withdraw:\n"))
        if(self.balance>amount):
            self.balance-=amount
            print("Available Balance is:\n",self.balance)
        else:
            print("Insuffitient Balance\n")
    def bal(self):
        print("Available Balance is:\n",self.balance)
obj=ac()
while True:
    op=int(input("\n1.Deposit Amount\n2.Withdraw Amount\n3.Balance\n4.Exit\nPlease Select An Option:\n"))
    if op==1:
        obj.depo()
    elif op==2:
        obj.withdraw()
    elif op==3:
        obj.bal()
    elif op==4:
        break
    else:
        print("Enter A Valid Option")

        