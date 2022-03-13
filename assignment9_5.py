 

def main():
    print("enter the file name : ")
    name = input()
    print("enter the word whose frequency you want to find  : ")
    i = input()
    
    fd = open(name,"r")
    data = fd.read()
    data1 = data.split(" ")
    
    jcount = 0
    for j in range(len(data1)):
        if data1[j]== i  : 
            jcount = jcount + 1 

    print("frequency of word is :",jcount)
    fd.close()
    
if __name__=="__main__":
    main()