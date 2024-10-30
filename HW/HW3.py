def generate_random_sequence(a, b, n, seed):
    import random
    random.seed(seed)
    d = [random.randint(a,b) for i in range(n)]
    return d   

def all_values_in_list(a, b, data):
    ans = False
    c = 0
    for i in range(a,b+1):
        if not i in data:
            c += 1
    if c == 0:
        ans = True
    return ans

def get_shortest_sequence_range(a, b, sequence):
    c = []
    d = []
    for i in range(len(sequence)):
        if a <= sequence[i] <= b:
            c.append(sequence[i])
    for i in range(a,b+1):
        k = c.index(i)
        d.append(k)
    a1 = min(d)
    a2 = max(d)
    ans = c[a1:a2+1:]
    return ans
    
def check_all_occurrence(value, n, data):
    c = 0
    for i in range(len(data)):
        if data[i] == value:
            c +=1
    if c >= n:
        return True
    else:
        return False
    
def generate_shortest_sequence_from_a2b(a, b, seed):
    import random
    random.seed(seed)
    sequence = [random.randint(a,b) for n in range(500)]
    x = get_shortest_sequence_range(a, b, sequence)
    return x
    
def get_unique_sequence(sequence):
    a = sequence[0]
    b = [a]
    for i in range(1,len(sequence)):
        if sequence[i] == a:
            pass
        elif sequence[i] != a and sequence[i] not in b :
            b.append(sequence[i])
            a = sequence[i]
    return b

def generate_course_hc_scales(seed):
    ans = []
    import random
    random.seed(seed)
    a = 1; b = 18
    sequence = [random.randint(a,b) for n in range(500)]
    x = get_unique_sequence(sequence)
    for i in x:
        if i%2 ==1:
            ans.append(i)
    for i in x:
        if i%2 ==0:
            ans.append(i)
    return ans
    
def holes_sorted_by_hc_scales(hc_scales):
    ans = []
    for i in range(1,19):
        k = hc_scales.index(i)
        ans.append(k+1)
    return ans


#check1 generate_random_sequence
#print(generate_random_sequence(2,5,10,2566))
#print(generate_random_sequence(2,5,20,2566))
#print(generate_random_sequence(2,6,10,2566))
#print(generate_random_sequence(2,6,20,2566))
#print(generate_random_sequence(1,9,10,2566))
#print(generate_random_sequence(1,18,10,2566))
#print(generate_random_sequence(2,5,10,2567))
#print(generate_random_sequence(2,6,10,2567))
#print(generate_random_sequence(1,9,10,2567))
#print(generate_random_sequence(1,18,10,2567))
#print(generate_random_sequence(1,18,20,2567))

#check2 all_values_in_list
#print(all_values_in_list(2,5,[2, 5, 3]))
#print(all_values_in_list(2,5,[2, 5, 3, 4]))
#print(all_values_in_list(2,5,[2, 8, 4, 6, 8, 5, 6, 1, 8, 2, 9, 9]))
#print(all_values_in_list(2,5,[2, 8, 4, 6, 8, 5, 6, 1, 8, 2, 9, 9, 3]))

#check3 get_shortest_sequence_range
#print(get_shortest_sequence_range(2,5,[2, 5, 3, 4, 5, 4, 4, 2, 5, 2, 6, 6, 3, 5, 4, 4, 6, 4, 6, 2]))
#print(get_shortest_sequence_range(2,6,[2, 5, 3, 4, 5, 4, 4, 2, 5, 2, 6, 6, 3, 5, 4, 4, 6, 4, 6, 2]))
#print(get_shortest_sequence_range(2,5,[2, 8, 4, 6, 8, 5, 6, 1, 8, 2, 9, 9, 3, 8, 6, 5, 9, 6, 2, 3]))
#print(get_shortest_sequence_range(2,6,[2, 8, 4, 6, 8, 5, 6, 1, 8, 2, 9, 9, 3, 8, 6, 5, 9, 6, 2, 3]))
#print(get_shortest_sequence_range(2,5,[4, 4, 4, 2, 5, 3, 5, 6, 2, 6, 5, 6, 6, 2, 6, 4, 2, 3, 2, 4]))
#print(get_shortest_sequence_range(2,6,[4, 4, 4, 2, 5, 3, 5, 6, 2, 6, 5, 6, 6, 2, 6, 4, 2, 3, 2, 4]))
#print(get_shortest_sequence_range(2,5,[6, 6, 6, 1, 8, 3, 8, 2, 9, 8, 9, 1, 9, 5, 1, 4, 1, 5, 6, 6]))
#print(get_shortest_sequence_range(2,6,[6, 6, 6, 1, 8, 3, 8, 2, 9, 8, 9, 1, 9, 5, 1, 4, 1, 5, 6, 6]))
    
#check4  check_all_occurrence
#print(check_all_occurrence(3,1,[2, 5, 3, 4, 5, 4, 4, 2, 5, 2]))
#print(check_all_occurrence(3,2,[2, 5, 3, 4, 5, 4, 4, 2, 5, 2]))
#print(check_all_occurrence(5,2,[2, 5, 3, 4, 5, 4, 4, 2, 5, 2]))
#print(check_all_occurrence(5,3,[2, 5, 3, 4, 5, 4, 4, 2, 5, 2]))
#print(check_all_occurrence(5,4,[2, 5, 3, 4, 5, 4, 4, 2, 5, 2]))

#check5 generate_shortest_sequence_from_a2b
#print(generate_shortest_sequence_from_a2b(2,5,2566))
#print(generate_shortest_sequence_from_a2b(2,5,2567))
#print(generate_shortest_sequence_from_a2b(2,6,2566))
#print(generate_shortest_sequence_from_a2b(2,6,2567))
#print(generate_shortest_sequence_from_a2b(1,9,2566))

#check6 get_unique_sequence
#print(get_unique_sequence([2, 5, 3, 4, 5, 4, 4, 2, 5, 2]))
#print(get_unique_sequence([5, 3, 6, 4, 3, 5, 4, 6, 3, 5, 4, 5, 6, 6, 3, 4, 6, 4, 6, 2]))
#print(get_unique_sequence([6, 6, 6, 1, 8, 3, 8, 2, 9, 8, 9, 1, 9, 5, 1, 4, 1, 5, 6, 6]))
#print(get_unique_sequence(generate_random_sequence(1, 18, 100, 2566)))
#print(get_unique_sequence(generate_random_sequence(1, 18, 100, 2567)))

#check7 generate_course_hc_scales
#print(generate_course_hc_scales(2566))
#print(generate_course_hc_scales(2567))

#check8 holes_sorted_by_hc_scales
#print(holes_sorted_by_hc_scales([17, 3, 13, 15, 5, 7, 9, 1, 11, 2, 6, 14, 16, 8, 12, 18, 4, 10]))
#print(holes_sorted_by_hc_scales([7, 11, 9, 1, 3, 5, 17, 13, 15, 4, 16, 18, 12, 10, 8, 2, 6, 14]))
#print(holes_sorted_by_hc_scales([11, 1, 15, 5, 3, 17, 9, 7, 13, 12, 18, 2, 8, 10, 16, 4, 6, 14]))
#print(holes_sorted_by_hc_scales([9, 3, 5, 7, 15, 13, 1, 17, 11, 16, 4, 12, 10, 8, 18, 14, 6, 2]))

#exec(input())