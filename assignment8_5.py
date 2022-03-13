import threading


def counter(func,lock):
    func(lock)

def fun (lock):
    print("using fun")
    lock.acquire()
    i=0
    while i<50:
        print(i)
        i= i+1
    lock.release()

def gun(lock):
    print("using gun")
    lock.acquire()
    for j in range(50,0):
        print(j)
    lock.release()    
    
def main():
  
    lock = threading.Lock()
    
    thread1 = threading.Thread(target=counter,args=(fun,lock,))
    thread2 = threading.Thread(target=counter,args=(gun,lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

if __name__ == "__main__":    
    main()