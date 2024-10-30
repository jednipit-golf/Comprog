A = input().split()
grade_sum=0
for i in A:
    if i == 'A':grade_sum+=4
    elif i == 'B':grade_sum+=3
    elif i == 'C':grade_sum+=2
    elif i == 'D':grade_sum+=1
    elif i == 'F':grade_sum+=0
    else:pass

print(grade_sum/len(A))