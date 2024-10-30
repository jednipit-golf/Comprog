a = input().split()
s1 = float(a[0])
s2 = float(a[1])
s3 = float(a[2])
s4 = float(a[3])
if s1 > s2:
    s1,s2 = s2,s1
if s3 > s4:
    s3,s4 = s4,s3
if s2 > s3:
    s2,s3 = s3,s2
if s1 > s2:
    s1,s2 = s2,s1
if s3 > s4:
    s3,s4 = s4,s3
S = (s2+s3)/2
print(round(S,2))