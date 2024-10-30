a = input()
n = int(input())
c = []
word = ''
for i in range(n):
    w = input().strip()
    W = len(w)
    c.append(W)
    word += w
max_c = max(c)
min_c = min(c)
k = len(word)
if max_c != min_c:
    print('Invalid size')
else:
    if a == '90':
        for i in range(W):
            ans = ''
            ans += word[(-W)+i::-W]
            print(ans)
    elif a == 'flip':
        for i in range(n):
            ans = ''
            ans += word[i*W:(i+1)*W:1]
            print(ans[::-1])
    elif a == '180':
        for i in range(n+1):
            ans = ''
            ans += word[k-(W*i):k-(W*i)+W:]
            print(ans[::-1])
            
    