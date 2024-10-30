def print_triangle(h):
    H = int(h)
    for i in range(H+1):
        if i == 0:
            a = '.'*(H-1)+'*'+'.'*((2*i)-1)
            print(a)
        elif 1 <= i < H-1:
            a = '.'*((H-i)-1)+'*'+'.'*((2*i)-1)+'*'
            print(a)
        elif i == (H):
            a = '*'*((2*i)-1)
            print(a)
        else: pass
exec(input())