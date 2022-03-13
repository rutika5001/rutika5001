class BankAccount :
    ROI = 10.5
    def __init__(self,a ,b):
        self.name = a
        self.account = b 
       
    def deposite(self):
        print("enter amount to be deposite:")
        x = int(input())
        self.account = self.account + x 
        
    def withdraw(self):
        print("enter amount to be withdraw:")
        y = int(input())
        self.account = self.account - y 
        
    def display(self):
        print("the name:",self.name)
        print("amount in the account:",self.account)
        
    
    def intrest(self):
        print("how many years you want intrest:")
        z = int(input())
        intrest = self.account * BankAccount.ROI * z / 100
        print("the rate of intrest is :",intrest)
        
def main():
    obj = BankAccount("Rutika Bhanuwanshe",50000)
    obj.deposite()
    obj.display()
    obj.withdraw()
    obj.display()
    obj.intrest()
  
    
    
    
if __name__ == "__main__":
    main()