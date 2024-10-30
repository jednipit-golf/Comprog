n = int(input())
p1 = 0
p2 = 0
T = 0
for i in range(3*n):
    x1,x2 = input().split()
    if x1 == 'R' and x2 == 'R':
        T +=1
    elif x1 == 'R' and x2 == 'P':
        p2 += 1
    elif x1 == 'R' and x2 == 'S':
        p1 += 1
    elif x1 == 'P' and x2 == 'R':
        p1 += 1
    elif x1 == 'P' and x2 == 'P':
        T +=1
    elif x1 == 'P' and x2 == 'S':
        p2 += 1
    elif x1 == 'S' and x2 == 'R':
        p2 += 1
    elif x1 == 'S' and x2 == 'P':
        p1 += 1
    elif x1 == 'S' and x2 == 'S':
        T +=1
    if p1 == n:
        ans = str(p1)+' '+str(p2)
        print(ans)
        print('Player 1 wins')
        break
    elif p2 == n:
        ans = str(p1)+' '+str(p2)
        print(ans)
        print('Player 2 wins')
        break
if p1 != n and p2 != n:
    ans = str(p1)+' '+str(p2)
    print(ans)
    print('Tie')
    
        
        
