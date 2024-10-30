x,y = input().split()
x,y =int(x),int(y)
min_zigzag = x
max_zigzag = y
max_zagzig = x
min_zagzig = y
i = 1
while True:
    d = input().split()
    if len(d) == 1: break
    i +=1
    x,y = int(d[0]),int(d[1])
    if i%2 == 0:
        x,y = y,x
        min_zigzag = min(x,min_zigzag)
        max_zigzag = max(y,max_zigzag)
        max_zagzig = max(x,max_zagzig)
        min_zagzig = min(y,min_zagzig)
    else:
        min_zigzag = min(x,min_zigzag)
        max_zigzag = max(y,max_zigzag)
        max_zagzig = max(x,max_zagzig)
        min_zagzig = min(y,min_zagzig)
if d[0] == 'Zig-Zag':
    print(min_zigzag,max_zigzag)
else:
    print(min_zagzig,max_zagzig)
        
    