import os

def main():
    print("enter the file name you want to check ")
    name = input()
    
    if os.path.exists(name):
        print("file exist")
    else:
        print("file doesn't exist ")
    

if __name__ == "__main__":
    main()
 