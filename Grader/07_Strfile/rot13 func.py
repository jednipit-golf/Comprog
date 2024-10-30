def rot_13(t):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot_13 = ''
    for e in t:
        if 'A' <= e <= 'Z':
            k = alphabet.find(e)
            if 0 <= k <= 12:
                rot_13 += alphabet[k+13]
            elif 13 <= k <= 25:
                rot_13 += alphabet[k-13]   
        else:
            rot_13 += e
    return rot_13

exec(input())