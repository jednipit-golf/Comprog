ID = []
grades = []

while True:
    a = input().split()
    if a[0] == 'q':
        break
    ID.append(a[0])
    grades.append(a[1])
k = input().split()
for i in k:
    if i in ID:
        a = ID.index(i)
        g = grades[a]
        if grades[a] == 'A':pass
        elif grades[a] == 'B+':
            grades[a] = 'A'
        elif grades[a] == 'B':
            grades[a] = 'B+'
        elif grades[a] == 'C+':
            grades[a] = 'B'
        elif grades[a] == 'C':
            grades[a] = 'C+'
        elif grades[a] == 'D+':
            grades[a] = 'C'
        elif grades[a] == 'D':
            grades[a] = 'D+'
        elif grades[a] == 'F':
            grades[a] = 'D'
for i in range(len(ID)):
    ans = ''
    ans += ID[i]+' '+grades[i]
    print(ans)
        