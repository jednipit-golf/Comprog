id_1,gpax_1,com_1,cal1_1,cal2_1 = input().split()
id_2,gpax_2,com_2,cal1_2,cal2_2 = input().split()
x = []
if com_1 == 'A' and cal1_1 <= 'C' and cal2_1 <= 'C':
    x += [id_1]
if com_2 == 'A' and cal1_2 <= 'C' and cal2_2 <= 'C':
    x += [id_2]
if len(x) == 0:
    print('None')
elif len(x) == 1:
    print(x[0])
else:
    if gpax_1 > gpax_2:
        print(id_1)
    elif gpax_2 > gpax_1:
        print(id_2)
    else:
        if cal1_1 > cal1_2:
            print(id_2)
        elif cal1_2 > cal1_1:
            print(id_1)
        else:
            if cal2_1 > cal2_2:
                print(id_2)
            elif cal2_2 > cal2_1:
                print(id_1)
            else:
                print('Both')
