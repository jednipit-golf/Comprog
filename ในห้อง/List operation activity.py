a = [float(i) for i in input().split()]
b=[]
for i in range(len(a)-1):
    if i != len(a):
        s = (a[i]+a[i+1])/2
    else: s = (a[-1]+a[-2])/2
    b.append(s)
c=0
for i in b:
    a.insert((2*c)+1,i)
    c+=1
print(a)