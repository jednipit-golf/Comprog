def index_of(grades, ID):
    c = 0
    for i in range(len(grades)):
        if grades[i][0] == ID:
            return i
            c += 1 
    if c == 0:
        return -1
def upgrade(grades, IDs):
    for i in range(len(grades)):
        for k in range(len(IDs)):
            if grades[i][0] == IDs[k]:
                if grades[i][1] == 'A':
                    pass
                elif grades[i][1] == 'B+':
                    grades[i] = [IDs[k],'A']
                elif grades[i][1] == 'B':
                    grades[i] = [IDs[k],'B+']
                elif grades[i][1] == 'C+':
                    grades[i] = [IDs[k],'B']
                elif grades[i][1] == 'C':
                    grades[i] = [IDs[k],'C+']
                elif grades[i][1] == 'D+':
                    grades[i] = [IDs[k],'C']
                elif grades[i][1] == 'D':
                    grades[i] = [IDs[k],'D+']
                elif grades[i][1] == 'F':
                    grades[i] = [IDs[k],'D']        
    return grades.sort()
exec(input())
exec(input())
exec(input())
