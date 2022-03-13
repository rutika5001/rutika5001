import os 

def main():
    print("enter the file name you want to open")
    name = input()
    
    if os.path.exists(name):
        fd = open(name,"r")
        
        data = fd.read()
        print("data from the file is : ",data)
        
        fd.close()
    else:
        print("file does not exist  ")

if __name__ == "__main__":
    main()