def displayN(i = 1):
   
   if i < 6 :
        print(i , end = " ")
        i = i + 1
        displayN(i)

def main():
    displayN()

if __name__ == "__main__":
    main()