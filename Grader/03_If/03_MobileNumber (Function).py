def is_mobile_number(number):
    if len(number)!=10:
        return False
    else:
        n = number[0:2]
        b = ['06','08','09']
        if n not in b:
            return False
        else:
            return True
    
exec(input())