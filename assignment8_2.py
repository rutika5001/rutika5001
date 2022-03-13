import threading

def counter(gun,no,lock):
    gun(no,lock)

def EvenFactor(no,lock):
    lock.acquire()
    for i in range(1,no):
        if no % i == 0:
            if i % 2 == 0 :
                print("even factor of number is :",i)
    lock.release()

def OddFactor(no,lock):
    lock.acquire()
    for i in range(1,no):
        if no % i == 0:
            if i % 2 != 0: 
                print("odd factor of number is : ",i)
    lock.release()            
    

def main():
    no = int(input("Enter the number : "))
    lock = threading.Lock()
   
    thread1 = threading.Thread(target=counter,args=(EvenFactor,no,lock,))
    thread2 = threading.Thread(target=counter,args=(OddFactor,no,lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    print("exit from main  ")
if __name__ == "__main__":
    main()