"""
class Book:     
    def __init__(self, title, isbn, price):             #__ชื่อฟังชั่น__
        self.title = title
        self.isbn  = isbn
        self.price = price

    
b1 = Book('Data Scince'    ,'149190142X',28.79)
b2 = Book('Learning Python','1449355730',37.06)
b3 = Book('Data Analysis'  ,'1449319793',27.68)
def total_price(book):
    s = 0
    for i in book:
        s += i.price
    return s
        
print(total_price([b1,b2,b3]))
"""

"""
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,p):
        dx = self.x-p2.x
        dy = self.y-p2.y
        a = ((dx**2)+(dy**2))**(0.5)
        return a
    def to_str(self):
        return "("+str(self.x)+','+str(self.y)+')'
    

class date:
    def __init__(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y
        
class song:
    def __init__(self,title,artist,lyrics):
        self.title  = title
        self.artist = artist
        self.lyrics = lyrics
        self.nviews = 0
p1 = point(2,4)
p2 = point(3,5)
#print(p1.distance(p2))
#print(p1.to_str())



#print(to_str(p1),to_str(p2))
#print('distance from '+to_str(p1)+' to '+to_str(p2)+':\n'+str(d))    
"""
"""
class bank:
    def __init__(self,acc,name,balance):
        self.acc     = acc
        self.name    = name
        self.balance = balance 
    def deposit(self,amout):
        self.balance += amout
    def withdraw(self,amout):
        self.balance -= amout
    def transfer(self,acc,amout):
        if 0 <= amout <= self.balance:
            self.withdraw(amout)
            acc.deposit(amout)
          
a1 = bank('135654212','golf',5000)
a2 = bank('135654213','kan',5000)
a1.transfer(a2,2000)
print('balance a1: '+str(a1.balance))
print('balance a2: '+str(a2.balance))
"""

class rational:
    def __init__(self,n,d):
        g = rational.gcd(n,d)
        self.n = n//g
        self.d = d//g
    def gcd(a,b):
        while b != 0:
            a,b = b,a%b
        return a
    def __mul__(self,x):
        n = self.n * x.n
        d = self.d * x.d
        return rational(n,d)
    def __add__(self,x):
        d = self.d * x.d
        n = (self.n * x.d) + (x.n * self.d)
        return rational(n,d)
    def __float__(self):
        return self.n / self.d
    def __lt__(self,x):
        return float(self) < float(x)
    def __str__(self):
        return str(self.n) + "/" + str(self.d)   
r1 = rational(20,40)
r2 = rational(1,4)
r3 = r1 + r2
r4 = r1 + r2
print(str(r3),float(r4))
print(r3 < r4)

"""
class Item:
    def __init__(self,name,price):
        self.name =  name
        self.price = price
    def __lt__(self,rhs):
        return self.price < rhs.price
    def __str__(self):
        return self.name + ":" + str(self.price)

class Order:
    def __init__(self):
        self.order_items = []
        self.paid = False
    def add(self,item,n):
        for i in range(n):
            self.order_items.append(item)
    def total(self):
        return sum([item.price for item in self.order_items])
def get_total(orders):
    return sum([od.total() for od in orders if od.paid])
m = [ Item('fried rice',45),
      Item('Phat thai',50),
      Item('congee',30),
      Item('papaya salad',40)]
o1 = Order()
o1.add(m[0],2);o1.add(m[3],1)
o2 = Order()
o2.add(m[0],1);o2.add(m[1],2);
o3 = Order()
o3.add(m[1],1);o3.add(m[2],1);

orders = [o1,o2,o3]
o1.paid = True
o2.paid = True
print(get_total(orders))
print(m[0]<m[1])
print(m[1])
"""













































































