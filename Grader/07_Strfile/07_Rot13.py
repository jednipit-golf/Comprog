alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
tt = []
ans = []
while True:
    t = input()
    if t == 'end':
        break
    tt.append(t)
rot_13 = ''
for i in range(len(tt)):
    for e in tt[i]:
        if 'A' <= e <= 'z':
            k = alphabet.find(e)
            if 0 <= k <= 12:
                rot_13 += alphabet[k+13]
            elif 13 <= k <= 25:
                rot_13 += alphabet[k-13]
            if 26 <= k <= 38:
                rot_13 += alphabet[k+13]
            elif 39 <= k <= 51:
                rot_13 += alphabet[k-13]
        else:
            rot_13 += e
    ans.append(rot_13)
    rot_13 = ''
for i in range(len(tt)):
    print(ans[i])


