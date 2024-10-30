a = input().strip()
z = open(a, 'r')
section = {}
teacher = []
ans = {}
k = []
m = 0
f = 0
for i in z:
    a = i.strip().split(',')
    if a[4]+a[3] in section:
        section[a[4]+a[3]] += a[0]+a[1]
    else:
        section[a[4]+a[3]] = a[0]+a[1]
    if a[4] in teacher:
        pass
    else:
        teacher.append(a[4])
ids = input().strip()
I = len(ids)
if ids in teacher:
    for i in section:
        if ids == i[0:I]:
            ans[i[I:]] = len(section[i])//11
            b = section[i]
            for i in b:
                if i == 'M':
                    m += 1
                elif i == 'F':
                    f += 1           
    if len(ans) == 1:
        for i in ans:
            print('Section: '+i+' --> F = '+str(f)+', M = '+str(m))
    else:
        for i in ans:
            k.append(i)
        print('Sections: '+','.join(k)+' --> F = '+str(f)+', M = '+str(m))
else:
    print('Not found')
        
        
        
    

    
        
        
        
    