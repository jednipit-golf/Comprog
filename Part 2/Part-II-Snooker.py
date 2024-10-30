s = {'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7}
on_table = 'RRRRRR'
p1 = 0
p2 = 0
while len(on_table) != 0:
    a = input().strip()
    if a[0] == '1':
        if len(a) == 2:
            pass
        else:
            if a[1] == 'R':
                on_table = on_table[1:len(on_table)]
                p1 += 1
            if a[2] == 'X':
                pass
            else:
                p1 += s[a[2]]
        
    elif a[0] == '2':
        if len(a) == 2:
            pass
        else:
            if a[1] == 'R':
                on_table = on_table[1:len(on_table)]
                p2 += 1
            if a[2] == 'X':
                pass
            else:
                p2 += s[a[2]]
                
last = 'YGWBPK'
while len(last) != 0:
    b = input().strip()
    if b[0] == '1':
        if b[1] == 'X':
            pass
        else:
            p1 += s[b[1]]
            h = last.find(b[1])
            last = last[:h]+last[h+1:]
    elif b[0] == '2':
        if b[1] == 'X':
            pass
        else:
            p2 += s[b[1]]
            h = last.find(b[1])
            last = last[:h]+last[h+1:]
ans_1 = str(p1)+' '+str(p2)
print(ans_1)
if p1 > p2:
    print('Player 1 wins')
elif p1 < p2:
    print('Player 2 wins')
elif p1 == p2:
    print('Tie')

            
        
        
        