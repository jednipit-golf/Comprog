class roman :
    def __init__(self, r):
        self.n = roman2int(r)
        
    def __lt__(self, rhs):
        return self.__int__() < rhs.__int__()    
    def __str__(self):
        return int2roman(self.n)   
    def __int__(self):
        c = 0
        a = self.r
        n = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        k = ['IV','IX','XL','XC','CD','CM']
        for i in range(len(a)):
            c += n[a[i]]
        for i in range(len(a)-1):
            if a[i:i+2] in k:
                c -= n[a[i:i+1]]*2
        return c    
    def __add__(self, rhs):
        return self.__int__()+rhs.__int__()
    def int2roman(a)

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
