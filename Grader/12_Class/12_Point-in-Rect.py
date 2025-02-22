class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2
    def area(self):
        x1 = self.lowerleft.x
        y1 = self.lowerleft.y
        x2 = self.upperright.x
        y2 = self.upperright.y
        return abs((x1-x2)*(y1-y2)) 
    def contains(self, p):
        x1 = self.lowerleft.x
        y1 = self.lowerleft.y
        x2 = self.upperright.x
        y2 = self.upperright.y
        X = p.x
        Y = p.y
        if (x1 <= X <= x2) and (y1 <= Y <= y2):
            return True
        elif (x1 <= X <= x2) and (y1 >= Y >= y2):
            return True
        elif (x1 >= X >= x2) and (y1 <= Y <= y2):
            return True
        elif (x1 >= X >= x2) and (y1 >= Y >= y2):
            return True
        else:
            return False

x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(rect.contains(p)) 
 