n = int(input())
c = []
x = []
y = []
text = []
T = ''
w = []
t = ''
for i in range(n):
    a = input().strip()
    c.append(a)
while True:
    w = input().strip()
    if w == 'END':
        break
    T += w+' '
    text.append(w)
j = 0
for i in range(len(T)):
    if T[i] == '*':
        a = T.find(T[i],i)
        j = a
        x.append(a)
        for k in c:
            if k in T[a+1:a+len(k)+2]:
                y.append(a)
for i in y:
    if i in x:
        a = x.index(i)
        a += 1
    ans = T[i:x[a]]
    print(ans.strip())

                
                

        
    
    
    
    

    
            