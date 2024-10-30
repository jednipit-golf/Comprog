def is_undergrad( sid ):
    if int(sid[2])==0 or int(sid[2])==3 or int(sid[2])==4:
        return True
    else:
        return False
def get_faculty( sid ):
    if sid[-2:] == '21':
        return "ENG"
    elif sid[-2:] == '22':
        return "ART"
    elif sid[-2:] == '23':
        return "SCI"
    else:
        return "OTHER"
def get_status(sid):
    if is_undergrad(sid) == True:
        ans = 'U'
    else:
        ans = 'G'
    return [ans,get_faculty(sid)]          
exec(input().strip())
