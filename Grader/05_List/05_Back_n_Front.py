ans = []
Ans = []
c1 = []
c2 = []
c3 = []
n = int(input())
while n>0:
    k = int(input())
    c1.append(k)
    n -=1
a = [int(e) for e in input().split()]
while True:
    b = int(input())
    if b == -1:
        break
    else:
        c2.append(b)
c3 += c1
c3 += a
c3 += c2
C = len(c3)
for i in range(C):
    if i%2 == 0:
        ans.append(c3[i])
    else:
        ans = [c3[i]] + ans
print(ans)