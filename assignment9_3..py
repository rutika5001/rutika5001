def main():
    print("enter the file name you want to create :")
    name = input()
    
    fd = open(name,"x")
    
    print("enter the file name you want to read")
    name1 = input()
    fd = open(name1,"r")
    data = fd.read(name1)
    
        for line in data :
        
            name.write(line)
            print("data copy is :",line)    
if __name__ == "__main__":
    main()