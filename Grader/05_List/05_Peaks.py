x = [int(e) for e in input().split()]
c = len(x)
k = 0
for i in range(1,c-1):
    if x[i-1] < x[i] and x[i] > x[i+1]:
        k += 1
    elif x[i-1] < x[i] and x[i] > x[i+1]:
        k += 1
print(k)