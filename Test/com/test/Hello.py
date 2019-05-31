class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
   def __sub__(self,other):
       return Vector(self.a - other.a, self.b - other.b)
   
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 - v2

#python 100 for 1
def test1():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if( i != k ) and (i != j) and (j != k):
                    print i,j,k
                    
#test1()


def test2():
    i = int(raw_input('test'))
    arr = [1000000,600000,400000,200000,100000,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    r = 0
    for idx in range(0,6):
        if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            print (i-arr[idx])*rat[idx]
            i=arr[idx]
    print r
   
test2()           