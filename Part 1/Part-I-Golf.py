import math
par = []
count_par = 0
par_add = []
stroke = []
count_stroke = 0
choose = []
compare_stroke = []
count_compare_stroke = 0
for i in range(9):
    a = [int(e) for e in input().split()]
    par.append(a[0])
    par_add.append(a[0]+2)
    stroke.append(a[1])
    choose.append(a[2])
for i in range(9):
    if choose[i] == 1:
        if par_add[i] < stroke[i]:
            compare_stroke.append(par_add[i])
        elif par_add[i] == stroke[i]:
            compare_stroke.append(par_add[i])
        elif par_add[i] > stroke[i]:
            compare_stroke.append(stroke[i])
n = len(compare_stroke)
for i in range(n):
    count_compare_stroke += compare_stroke[i]
for i in range(9):
    count_par += par[i]
    count_stroke += stroke[i]
handicap = math.floor((0.8*((1.5*count_compare_stroke)-count_par)))
final_score = count_stroke - handicap
print(count_stroke)
print(handicap)
print(final_score)
    
    