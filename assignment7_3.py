i = 5 
def displayX():
    global i 
    if i > 0 :
        print(i , end = " ")
        i = i - 1
        displayX()
        
def main():
    displayX()

if __name__ == "__main__":
    main()