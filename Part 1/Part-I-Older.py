a = input().split()
b = input().split()
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
if a[1] == 'January':
    month_a = 1
elif a[1] == 'February':
    month_a = 2
elif a[1] == 'March':
    month_a = 3
elif a[1] == 'April':
    month_a = 4
elif a[1] == 'May':
    month_a = 5
elif a[1] == 'June':
    month_a = 6
elif a[1] == 'July':
    month_a = 7
elif a[1] == 'August':
    month_a = 8
elif a[1] == 'September':
    month_a = 9
elif a[1] == 'October':
    month_a = 10
elif a[1] == 'November':
    month_a = 11
elif a[1] == 'December':
    month_a = 12
    
if b[1] == 'January':
    month_b = 1
elif b[1] == 'February':
    month_b = 2
elif b[1] == 'March':
    month_b = 3
elif b[1] == 'April':
    month_b = 4
elif b[1] == 'May':
    month_b = 5
elif b[1] == 'June':
    month_b = 6
elif b[1] == 'July':
    month_b = 7
elif b[1] == 'August':
    month_b = 8
elif b[1] == 'September':
    month_b = 9
elif b[1] == 'October':
    month_b = 10
elif b[1] == 'November':
    month_b = 11
elif b[1] == 'December':
    month_b = 12
year_a = a[3]
year_b = b[3]
d_a = int(a[2][:-1])
d_b = int(b[2][:-1])
if year_a == year_b:
    if month_a == month_b:
        if d_a == d_b:
            x = a[0]+' '+b[0]
            print(x)
        elif d_a > d_b:
            print(b[0])
        elif d_a < d_b:
            print(a[0])
    elif month_a > month_b:
        print(b[0])
    elif month_a < month_b:
        print(a[0])
elif year_a > year_b:
    print(b[0])
elif year_a < year_b:
    print(a[0])