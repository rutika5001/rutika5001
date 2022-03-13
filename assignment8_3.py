import threading
isum = 0
jsum = 0

def counter(fun,data,lock):
    fun(data,lock)
    
def Even(data,lock):
    lock.acquire()
    global isum
    for i in range (len(data)):
        if data [i] % 2 == 0 : 
            isum = isum + data[i]
    print("sum of even number is : ", isum)
    lock.release()
    
def Odd(data,lock):
    lock.acquire() 
    global jsum 
    for i in range(len(data)):
        if data[i] % 2  != 0:
            jsum = jsum + data[i]
    print("sum of odd number is : ",jsum)
    lock.release()

def main():
    data = [24,2,5,11,13,88,6,68,70]
    lock = threading.Lock()
    
    Evenlist = threading.Thread(target=counter,args=(Even,data,lock))
    Oddlist = threading.Thread(target=counter,args=(Odd,data,lock))
    
    Evenlist.start()
    Oddlist.start()
    
    Evenlist.join()
    Oddlist.join()
    
   
  

if __name__ == "__main__":
    main()
    