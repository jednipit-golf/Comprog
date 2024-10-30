birth1 = input().split()
birth2 = input().split()
d1,m1,y1 = birth1[1].split('/')
d2,m2,y2 = birth2[1].split('/')
d1 = int(d1)
d2 = int(d2)
m1 = int(m1)
m2 = int(m2)
y1 = int(y1)
y2 = int(y2)
if y1 > y2 :
    print(birth2[0])
elif y1 < y2 :
    print(birth1[0])
elif (y1==y2) and (m1>m2):
    print(birth2[0])
elif (y1==y2) and (m1<m2):
    print(birth1[0])
elif (y1==y2 and m1==m2) and (d1 > d2):
    print(birth2[0])
elif (y1==y2 and m1==m2) and (d1 < d2):
    print(birth1[0])
elif (y1==y2 and m1==m2) and (d1 == d2):
    print(birth1[0],birth2[0])