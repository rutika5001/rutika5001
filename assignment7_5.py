i = 1
imul = 1

def display(no):
    global i 
    global imul
    if  i <= no: 
        imul = imul * i
        i = i + 1
        display(no)  
    return imul    
    
    

def main():
    no = int(input("Enter the number :"))
    ret = display(no)
    print("factorial is :",ret)
   

if __name__ == "__main__":
    main()