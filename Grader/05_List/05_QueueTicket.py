q = []
n = int(input())
number = 0
time_use = []
for i in range(n):
    c = input().split()
    if c[0] == 'reset':
        number = int(c[1])
    elif c[0] == 'new':
        print('ticket '+str(number))
        q.append([number,c[1]])
        number+=1
    elif c[0] == 'next':
        a = q.pop(0)
        print('call '+str(a[0]))
    elif c[0] == 'order':
        t = int(c[1])- int(a[1])
        time_use.append(t)
        print('qtime '+str(a[0])+' '+str(t))
    elif c[0] == 'avg_qtime':
        total = sum(time_use)/len(time_use)
        print('avg_qtime ',str(round(total,4)))
            
        
    