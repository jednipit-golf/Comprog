
x = '---------------------------------------------------------------------'
import numpy as np
"""
a = np.array([1,2,3,4])             #vector
b = np.array([[1,2],[3,4]],float)
c = np.ndarray((2,3), int) #n-diamentional row x colum
e = np.zeros((2,3),int)
f = np.ones((2,3),int)
g = np.zeros_like(f,float) #ตามมิติ f
h = np.ones_like(e,float) #ตามมิติ e
i = np.identity(4,int) #เมตริก เอกลักษษณ์
o = np.arange(0.0,1.0,0.1)
print('a : np.array([1,2,3,4]')
print(a)
print(x)
print('b : np.array([[1,2],[3,4]],float)')
print(b)
print(x)
print('c : np.ndarray((2,3), int)')
print(c)
print(x)
print('e : np.zeros((2,3),int)')
print(e)
print(x)
print('f : np.ones((2,3),int)')
print(f)
print(x)
print('g : np.zeros_like(f,float) np.zeros_like(f,float)')
print(g)
print(x)
print('h : np.ones_like(e,float)')
print(h)
print(x)
print('i : np.identity(4,int)')
print(i)
print(x)
print('o : np.arange(0.0,1.0,0.1)')
print(o)
print(x)
a = np.arange(8)
b = a.reshape(1,8)
print(a)
print(x)
print(b)
print(x)
"""
def counts_ones(a):
    c = 0
    if len(a.shape) == 2:
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                if a[i,j] == 1:
                    c += 1
        return c
    else:
        return 'a isn\'t matrix'
"""
a = np.arange(1,13)
a = a.reshape(4,3)
A = a
"""
"""
a = np.array([[1,2,3],[4,5,6],[7,8,9],[0,1,0]])
b = a[[1,3,2],[2,0,1]] #a[1,2] , a[3,0] , a[2,1]
a = np.ndarray((4,4),int)
for i in range(4):
    for j in range(i,4):
        a[i,j] = 25
for i in range(3):
    for j in range(i+1,4):
        a[j,i] = 5
n = int(input())
a = np.ndarray((n,n),int)
for i in range(n):
    for j in range(n):
        if i%2 == 0:
            if j%2 == 0:
                a[i,j] = 2
            else:
                a[i,j] = 1
        else:
            if j%2 == 1:
                a[i,j] = 2
            else:
                a[i,j] = 1
print(a)
j = []
for i in range(10):
    j.append(i)
a = np.array(j)
a = a.reshape(5,2)
b = a*5
c = b+a
d = np.sin(c/2)
i = np.identity(3,int)   #nu
a = np.array([1,2,3,4,5,6])
a = a.reshape(2,3)
b = np.array([5,3,6,8,6,2])
b = b.reshape(2,3)
c = a*b
print(c)
"""
def counts_odd(a):
    return sum(a%2==1)
"""
m1 = np.array([[-7,2],[-5,7],[-1,0]])
t = np.zeros_like(m1,int)
a = t.shape
t[:,0:1] = 7
t[:,1:2] = -3
c = m1 + t
print('m1 is: \n',m1)
print(x)
print('t is: \n',t)
print(x)
print('m1 + t is: \n',c)
"""
"""
a = np.array([[2,2],[3,3],[4,4]])
b = np.array([[2,2]])
print(a+b)
"""
"""
j = [i for i in range(1,21)]
b = np.array(j)
b = b.reshape(4,5)
print(b)
print(x)
print('ผลบวกตามแนวคอลลัม คือ axis = 0:\n',np.sum(b,axis = 0))
print(x)
print('ผลบวกตามแนวแถว คือ axis = 1:\n',np.sum(b,axis = 1))
print(x)
print('ค่าน้อยสุด ใช้ axis ได้') #argmin max ออกเป็นตำแหน่ง
print(np.min(b))
print(np.min(b,axis = 0))
print(np.min(b,axis = 1))
print(x)
print(np.mean(b,axis = 0))
print(np.std(b,axis = 0))
print(x)
 
a = np.array([[1,2,5],[3,4,6],[5,6,8]])
b = np.array([[1,2,3,6,7],[3,4,5,7,8],[5,6,8,8,0]])
print(a)
print(x)
print(b)
print(x)
print(np.dot(a,b))
"""
#กับข้าว
"""
n = int(input()) 
j = []
k = []
for i in range(n):
    a = int(input('ใส่ราคาข้าว '))
    j.append(a)
print(x)
for f in range(n):
    a = [int(i) for i in input().split()]
    for i in a:
        k.append(i)
    print(x)
b = np.array(k)
b = b.reshape(n,5)    
j = np.array(j)
worth = j.dot(b)
print('worth: ',worth)
print('MO --> ',worth[0])
print('TH --> ',worth[1])
print('WE --> ',worth[2])
print('TH --> ',worth[3])
print('FR --> ',worth[4])
print('weekly in come :',sum(worth))
print('daily average :',np.mean(worth))
b = np.argmax(worth)
print('best sale :',worth[b])
"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    

