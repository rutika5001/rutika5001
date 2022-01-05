class circle :
    PI = 3.14

    def __init__(self,x,a,b):
        self.radius = x
        self.area = a
        self.circumference = b 

    def accept(self):
        print("enter the radius :")
        x = float(input())
        return x 

    def calculatearea(self):
        area = circle.PI * self.radius * self.radius
        return area
    
    def calculatecircumfernce(self):
        circumference = 2 * circle.PI * self.radius
        return circumference

    def display(self,ret,ret1,ret2):
        print("radius of circle is :",self.radius)
        print("area of circle is :",ret1)
        print("circumference of circle is :",ret2)    

def main():
   
    obj = circle(0.0,0.0,0.0)
    ret = obj.accept()
    
    obj1 = circle(ret,0.0,0.0)
    ret1 = obj1.calculatearea()
    ret2 = obj1.calculatecircumfernce()
    
    obj2 = circle(ret,ret1,ret2)
    obj2.display(ret,ret1,ret2)

if __name__ =="__main__":
    main()
    
    