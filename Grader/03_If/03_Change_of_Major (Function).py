def choose(stu1, stu2):
    status_1 = False
    status_2 = False
    A0 = []
    A1 = [stu1[0]]
    A2 = [stu2[0]]
    A3 = [stu1[0],stu2[0]]
    g1 = [stu1[2],stu1[3],stu1[4]]
    g2 = [stu2[2],stu2[3],stu2[4]]
    if g1[0] == 'A' and g1[1] <= 'C' and g1[2] <= 'C':
        status_1 = True
    if g2[0] == 'A' and g2[1] <= 'C' and g2[2] <= 'C':
        status_2 = True
    if status_1 == False and status_2 == False:
        return A0
    elif status_1 == True and status_2 == False:
        return A1
    elif status_2 == True and status_1 == False:
        return A2
    else:
        if stu1[1:] == stu2[1:]:
            return A3
        elif stu1[1] > stu2[1]:
            return A1
        elif stu2[1] > stu1[1]:
            return A2
        else:
            if g1[1] > g2[1]:
                return A2
            elif g2[1] > g1[1]:
                return A1
            elif g1[1] == g2[1]:
                if g1[2] > g2[2]:
                    return A2
                elif g2[2] > g1[2]:
                    return A1
                
    

exec(input()) 