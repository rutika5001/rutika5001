import os
def main():
    print("enter the file name you want to read")
    name1 = input()
    fd = open(name1,"r")
    data = fd.readline()
    fd.close()
    
    print("enter the file name you want to create :")
    name = input()
    fd = open(name,"w")
    
    for i in data :
        fd.write(i)
       
    fd.close()    
    print("data copide") 
    
        
if __name__ == "__main__":
    main()