word = []
n = int(input())
for i in range(n):
    o = []
    w = input()
    t = input().split()
    word.append([w,t])
while True:
    s = input()
    if s == '-1':
        break
    ans = []
    for i in word:
        name = i[0]
        text = i[1]
        ss = []
        c = 0
        for j in text:
            if j not in ss:
                ss.append(j)
            if j == s:
                c += 1
        f = c/len(text)
        sp_score = 1/len(ss)
        ss = []
        wa = f * sp_score
        c = 0
        ans.append([wa,name])
    ans.sort()
    z = ans[-1]
    if z[0] == 0:
        print('NOT FOUND')
    else:
        print(z[1])

        

            
            
        