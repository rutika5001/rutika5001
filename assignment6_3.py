class Numbers:
    
    def __init__ (self,a):
        self.no = a
        
    def chkprime (self):
        if self.no % 2 == 0 or self.no %3 == 0 :
            print("false")
        else:    
            print("true")
            
    def chkperfect(self):
        iper = 0
        
        for i in range (1,self.no):
            if self.no % i == 0:
                iper = iper + i
                
        if iper == self.no:
            print("number is perfect")
        else:
            print("number is not perfect")
        
        
    def factor (self):
        ifac = 0
        for i in range (1,self.no):
            if self.no % i == 0 :
                ifac = i 
                print(ifac)    
            
    def sumfactor(self):
        isum = 0
        for i in range  (1,self.no):
            if self.no % i == 0 :
                isum = isum + i 
        print(isum)

def main():
    print("Enter the number:")
    x = int(input())
    
    obj = Numbers(x)
    obj.chkprime()
    obj.chkperfect()
    obj.factor()
    obj.sumfactor()

if __name__ == "__main__":
    main()
