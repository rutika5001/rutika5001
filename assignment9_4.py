
import hashlib
def hashfile(path,blocksize = 1024):
    afile = open(path,"rb")
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
    
def main():
    print("enter the two file name : ")
    name1 = input()
    name2= input()
    
    i = hashfile(name1)
    j = hashfile(name2)
    
    if i == j :
        print("success")
    else:
        print("failure")
    
    
if __name__ == "__main__":
    main()