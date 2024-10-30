n = int(input())
i = 0
A = []
while i < n:
    a = input().split()
    A += a
    i +=1
B = input()
red = []
blue = []
if B == 'Zig-Zag':
    for k in range(2*n):
        if k%4 == 0 or k%4 == 3:
            red += [int(A[k])]
        else:    
            blue += [int(A[k])]
    
    min_red = min(red)
    max_blue = max(blue)
    print(min_red,max_blue)
elif B == 'Zag-Zig':
    for k in range(2*n):
        if k%4 == 0 or k%4 == 3:
            blue += [int(A[k])]
        else:    
            red += [int(A[k])]
    min_red = min(red)
    max_blue = max(blue)
    print(min_red,max_blue)
