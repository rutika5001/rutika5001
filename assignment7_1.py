i = 0
def display():
    global i 
  
    if i < 5 :
        print("*", end = " ")
        i = i + 1
        display()        


def main():
    display()

if __name__ == "__main__":
    main()