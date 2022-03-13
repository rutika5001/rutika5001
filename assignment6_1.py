class Bookstore:
    N_count = 0
    
    def __init__(self,a,b):
        self.name = a
        self.author = b
        Bookstore.N_count += 1
            
    
    def display(self):
        print("name of book is:",self.name)
        print("author of book is:",self.author)
        print("no of books is :",Bookstore.N_count)
    

def main():
    obj1 = Bookstore("Linus system Programming","Robert Love")
    obj1.display()
    
    obj2 = Bookstore("C Programming","dennis Ritchie")
    obj2.display()
    print("finish")
    
if __name__ == "__main__":
    main()