dict1 = {}
while True:
    a = input()
    if a == 'q':
        break
    name,animal = a.split(',')
    name = name.strip()
    animal = animal.strip()
    if animal not in dict1:
        dict1[animal] = name
    else:
        dict1[animal] = dict1[animal]+', '+name
for i in dict1:
    p = dict1[i]
    print(i+': '+p)