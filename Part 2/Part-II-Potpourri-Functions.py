def convex_polygon_area(p):
    x = []
    y = []
    for i in p:
        a,b = i
        x.append(a)
        y.append(b)
    X = 0
    Y = 0    
    for i in range(len(p)):
        if i == len(p) - 1:
            X += x[i]*y[0]
            Y += y[i]*x[0]
        else:
            X += x[i]*y[i+1]
            Y += y[i]*x[i+1]
    ans = abs((1/2)*(X-Y))
    return ans
       
def is_heterogram(s):
    ans = True
    word = ''
    k = ''
    s = s.lower()
    for i in s:
        if 'a' <= i <='z':
            k += i      
    for i in k:
        if i not in word:
            word += i
        else:
            ans = False
    return ans

def replace_ignorecase(s, a, b):
    x = len(a)
    k = 0
    new = []
    while k < len(s):
        if a.lower() == s[k:k+x].lower():
            new.append(b)
            k += x
        else:
            new.append(s[k])
            k += 1
    ans = ''.join(new)
    return ans
    
def top3(v):
    c = {}
    ans = []
    for i,s in v.items():
        if s not in c:
            c[s] = i
        else:
            c[s] = c[s] + i
    a = sorted(c)[::-1]
    for i in a:
        if len(c[i]) == 1:
            ans.append(c[i])
        else:
            name = []
            for ll in range(len(c[i])):
                k = c[i][ll]
                name.append(k)
            name.sort()
            for zz in name:
                ans.append(zz)
        ans = ans[0:3]
    return ans
        









for k in range(2):
    exec(input().strip())