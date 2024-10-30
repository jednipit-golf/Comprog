def no_lower(t):
    for i in t:
        if 'a'<=i<='z':
            return False
    return True

def no_upper(t):
    for i in t:
        if 'A'<=i<='Z':
            return False
    return True
            
def no_number(t):
    for i in t:
        if '0'<=i<='9':
            return False
    return True
    
def no_symbol(t):
    for i in t:
        if not ('0'<=i<='9' or 'a'<= i.lower() <='z'):
            return False
    return True

def char_repetition(t):
    for i in range(len(t)-3):
        if t[i]==t[i+1]==t[i+2]==t[i+3]:
            return True
    return False

def check_seq(t,seq,n):
    for i in range(len(t) - n + 1):
        if t[i:i+n].lower() in seq:
            return True
    return False

def letter_seq(t):
    seq = 'abcdefghijklmnopqrstuvwxyz'
    if check_seq(t,seq,4) == True:
        return True
    return check_seq(t,seq[::-1],4)

def number_seq(t):
    seq = '01234567890'
    if check_seq(t,seq,4) == True:
        return True
    return check_seq(t,seq[::-1],4)

def keyboard_seq(t):
    seq = '!@#$%^&*()_+\nqwertyuiop\n' + \
          'asdfghjkl\nzxcvbnm'
    if check_seq(t,seq,4) == True:
        return True
    return check_seq(t,seq[::-1],4)

passw = input().strip()
e = []
if len(passw) < 8:
    e.append("Less than 8 characters")
if no_lower(passw) == True:
    e.append("No lowercase letters")
if no_upper(passw) == True:
    e.append("No uppercase letters")
if no_number(passw) == True:
    e.append("No numbers")
if no_symbol(passw) == True:
    e.append("No symbols")
if char_repetition(passw) == True:
    e.append("Character repetition")
if number_seq(passw) == True:
    e.append("Number sequence")
if letter_seq(passw) == True:
    e.append("Letter sequence")
if keyboard_seq(passw) == True:
    e.append("Keyboard pattern")
if len(e) == 0:
    print('OK')
else:
    for i in range(len(e)):
        print(e[i])
    















