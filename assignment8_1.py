import threading


def counter(fun,lock):
    fun(lock)

def checkEven(lock):
    lock.acquire()
    
    for i in range (20):
        if i % 2  == 0: 
            print("even number : ",i)
    lock.release()
    
def checkOdd(lock):
    lock.acquire()
    
    for i in range(20):
        if i % 2 != 0 :
            print("odd number : ",i)
    lock.release()
    
def main():
    
   
    lock = threading.Lock()
    
    even = threading.Thread(target=counter,args=(checkEven,lock,))
    odd = threading.Thread(target=counter,args=(checkOdd,lock,))
    
    even.start()
    odd.start()
    
    even.join()
    odd.join()
    

if __name__ == "__main__":
    main()
