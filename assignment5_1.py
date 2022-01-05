class demo:
    value = 55
    
    def __init__(self,a,b):
        self.no1 = a
        self.no2 = b
    def fun(self):
        print("value of no1 from obj:",self.no1)
        
       
    def gun(self):
        print("value of no2 from obj:",self.no2)
        
    
def main():
    obj1 = demo(11,21)
    obj2 = demo(51,101)
    print(demo.value)
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()
    

if __name__ == "__main__":
    main()