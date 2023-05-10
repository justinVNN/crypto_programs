import numpy as np
class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

# check if point lies on the curve
def isPoint(a1):
    y=a1.y*a1.y
    y=np.mod(y,p)
    x=(a1.x*a1.x*a1.x + a*a1.x + b)
    x=np.mod(x,p)
    if(x==y):
        return True
    else:
        return False

# print all point on the curve
def allPoints(p,a,b):
    for i in range(0, p):
        for j in range(0,p):
            a2=Point(i,j)
            if(isPoint(a2)==True):
                print((i,j))

if __name__ == "__main__":
    a = 0
    b = -2
    p = 5
    print("All Points on the curve are :")
    print(allPoints(p,a,b))