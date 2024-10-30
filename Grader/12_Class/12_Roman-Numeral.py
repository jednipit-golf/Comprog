class roman :
    def __init__(self, r):
        rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = rom[r[0]]
        for i in range(1,len(r)):
            n += rom[r[i]]
            if rom[r[i]] > rom[r[i-1]]:
                n -= 2*rom[r[i-1]]
        self.n = n
    def __lt__(self, rhs):
        return self.n < rhs.n  
    def __str__(self):
        vals = [(1000,'M'),(900,'CM'),(500,'D'),
                (400,'CD'),(100,'C'),(90,'XC'),
                (50,'L'),(40,'XL'),(10,'X'),
                (9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        r = ''
        n = self.n
        for v,c in vals:
            k = n//v
            r += k*c
            n -= k*v
            if n ==0:break
        return r
    def __int__(self):
        return self.n    
    def __add__(self, rhs):
        n = self.n + rhs.n
        r = roman('I')
        r.n = n
        return r
    
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
