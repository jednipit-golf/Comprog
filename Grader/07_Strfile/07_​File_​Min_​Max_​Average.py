d,year = input().split()
o = int(year[2:4:])
a = open(d,'r')
ID = []
score = []
for i in a:
    x,y = i.split()
    y = float(y)
    ID.append([x,y])
ID.sort()
ans = []
for i in range(len(ID)):
    if ID[i][0][0:2] == str(o):
        ans.append(ID[i][1])
    else:
        pass
if len(ans) == 0:
    print('No data')
else:
    min_a = min(ans)
    max_a = max(ans)
    avg_a = sum(ans)/len(ans)
    ANS = str(min_a)+' '+str(max_a)+' '+str(avg_a)
    print(ANS)
a.close()