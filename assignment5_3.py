class arithemetic:
    def __init__(self,a,b):
        self.value1 = a 
        self.value2 = b
        
    def accept(self):
        print("enter the first number:")
        x = int(input())
        print("enter the second number:")
        y  = int(input())
        return x , y
       
            
        
    def addition(self):
        add = self.value1+ self.value2
        return add
        
    def substraction(self):
        sub = self.value1 - self.value2
        return sub
        
    def multipliction(self):
        mult = self.value1 * self.value2
        return mult
        
    def division(self):
        div = self.value1 / self.value2
        return div

def main():
    obj = arithemetic(0,0)
    
    ret1,ret2 = obj.accept()
    obj1 = arithemetic(ret1,ret2)
    
    ret3 = obj1.addition()
    print("addition is :",ret3)
    
    ret4 = obj1.substraction()
    print("substraction is:",ret4)
    
    ret5 = obj1.multipliction()
    print("multipliction is :",ret5)
    
    ret6 = obj1.division()
    print("division is :",ret6)
    
    

if __name__ == "__main__":
    main()