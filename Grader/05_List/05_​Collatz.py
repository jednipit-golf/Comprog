n = int(input())
A = [n]
ans =''
while n != 1:
    if n %2 == 0:
         n = n // 2 # ปัดเศษทิ้ง
    else:
         n = 3*n + 1
    A.append(n)
if len(A) > 15:
    A = A[-15:]
for i in range(len(A)):
    ans += str(A[i])+'->'
print(ans[:-2])
    