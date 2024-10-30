#HW2_Genetics_Analysis
def get_acgt_count(data):
    A = 0
    C = 0
    G = 0
    T = 0
    for i in data:
        if i == 'A':A+=1
        elif i == 'C':C+=1
        elif i == 'G':G+=1
        elif i == 'T':T+=1
        else:pass
    return [A,C,G,T]

def get_ag_ct_ratio(data):
    F = -1.0
    X = get_acgt_count(data)
    AG =int(X[0])+int(X[2]);CT=int(X[1])+int(X[3])
    if CT == 0:
        return F
    else:
        G = AG/CT
        return G
 
def get_gc_percentage(data):
    Y = get_acgt_count(data)
    count = int(len(data))
    G_and_C_count = Y[1]+Y[2]
    percent = (G_and_C_count)/count
    return percent

#def get_repeat_count(data, pattern):
#    count = 0
#    k = len(data)
#    for i in range(k-1):
#        if data[i:i+2] == pattern and data[i] != data[i+1]:
#            count += 1
#            if data[i+2:i+4] != pattern and count == 1:
#                return 0
#    return count

#def get_repeat_count(data, pattern):
#    count = 0
#   k = len(data)
#    for i in range(k-1):
#        if data[i:i+2] == pattern and data[i] != data[i+1]:
#            count += 1
#            if data[i:i+4] != pattern*2 and count == 1:
#                count = 0
#    return count
def get_repeat_count(data, pattern):
    for i in range(len(data) - 1):
        if data[i:i + 2] == pattern:
            count = 1
            j = i + 2
            while j < len(data) - 1:
                if data[j:j + 2] == pattern:
                    count += 1
                    j += 2
                else:
                    break
            if count >= 2:
                return count
            else:
                count = 0
    return 0
print(get_repeat_count("TGACACACGG", "AC"))  # Should return 3
print(get_repeat_count("ACAC", "AC"))        # Should return 2
print(get_repeat_count("CACACACA", "AC"))    # Should return 3
print(get_repeat_count("GACTACCAC", "AC"))   # Should return 0
print(get_repeat_count("ACTTACAC", "AC"))   # Should return 2
print(get_repeat_count("ACACTTAC", "AC"))   # Should return 2
print(get_repeat_count("ACACTTACTTAC", "AC"))   # Should return 2
print(get_repeat_count("ACTTACACTTAC", "AC"))   # Should return 2
print(get_repeat_count("ACTTACTTACAC", "AC"))   # Should return 2
print(get_repeat_count("ACTTACACACTTAC", "AC"))   # Should return 3
