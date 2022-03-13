i = 0
isum =  0 
j = int ,0 
def display(no):
    global j
    global i 
    global isum
    if no> 0 :
        i = no % 10
        isum = isum + i
        j = no / 10
        display(j)
    return isum    
        

def main():
    no = int(input("enter the number :"))
    ret = display(no)
    print(ret)

if __name__ == "__main__":
    main()
    
    
    