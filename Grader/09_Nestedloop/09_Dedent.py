n = int(input())
z = []
ans = []
for i in range(n):
    k = input()
    z.append(k)
for i in z:
    if len(i)>0:
        if i[0] == '.':
            c = 0
            for k in range(len(i)):
                if i[k] == '.':
                    c += 1
                else:
                    break
            c = c//2  
            ans.append(i[c::])
        else:
            ans.append(i)
    else:
        ans.append(i)
for i in ans:
    print(i)