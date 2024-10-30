a = input()
A = a[0]+a[1]
x = ['06','08','09']
if len(a) !=10:
    print('Not a mobile number')
else:
    if A not in x:
        print('Not a mobile number')
    else:
        print('Mobile number')