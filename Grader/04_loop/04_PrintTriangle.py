h = int(input())
for i in range(h+1):
    if i == 0:
        a = '.'*(h-1)+'*'+'.'*((2*i)-1)
        print(a)
    elif 1 <= i < h-1:
        a = '.'*((h-i)-1)+'*'+'.'*((2*i)-1)+'*'
        print(a)
    elif i == (h):
        a = '*'*((2*i)-1)
        print(a)
    else: pass