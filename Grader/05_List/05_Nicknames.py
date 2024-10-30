name = ['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
nick = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
ans = []
n = int(input())
c1 = []
for i in range(n):
    k = input()
    c1.append(k)
for i in range(n):
    if c1[i] == 'Robert':
        print('Dick')
    elif c1[i] == 'William':
        print('Bill')
    elif c1[i] == 'James':
        print('Jim')
    elif c1[i] == 'John':
        print('Jack')
    elif c1[i] == 'Margaret':
        print('Peggy')
    elif c1[i] == 'Edward':
        print('Ed')
    elif c1[i] == 'Sarah':
        print('Sally')
    elif c1[i] == 'Andrew':
        print('Andy')
    elif c1[i] == 'Anthony':
        print('Tony')
    elif c1[i] == 'Deborah':
        print('Debbie')
    elif c1[i] == 'Dick':
        print('Robert')
    elif c1[i] == 'Bill':
        print('William')    
    elif c1[i] == 'Jim':
        print('James')
    elif c1[i] == 'Jack':
        print('John')
    elif c1[i] == 'Peggy':
        print('Margaret')
    elif c1[i] == 'Ed':
        print('Edward')
    elif c1[i] == 'Sally':
        print('Sarah')
    elif c1[i] == 'Andy':
        print('Andrew')
    elif c1[i] == 'Tony':
        print('Anthony')
    elif c1[i] == 'Debbie':
        print('Deborah')
    else:
       print('Not found')
    

