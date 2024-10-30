def to_Thai(N):
    out=''
    t=str(N)
    if N>=1000:
        if N//1000==9:
            out+= 'kao'
            out+=' pun '
        elif N//1000==8:
            out+= 'paet'
            out+=' pun '
        elif N//1000==7:
            out+= 'chet'
            out+=' pun '
        elif N//1000==6:
            out+= 'hok'
            out+=' pun '
        elif N//1000==5:
            out+= 'ha'
            out+=' pun '
        elif N//1000==4:
            out+= 'si'
            out+=' pun '
        elif N//1000==3:
            out+= 'sam'
            out+=' pun '
        elif N//1000==2:
            out+= 'song'
            out+=' pun '
        elif N//1000==1:
            out+='neung'
            out+=' pun '
        N%=1000
    if N>=100:
        if N//100==9:
            out+= 'kao roi '
        elif N//100==8:
            out+= 'paet roi '
        elif N//100==7:
            out+= 'chet roi '
        elif N//100==6:
            out+= 'hok roi '
        elif N//100==5:
            out+= 'ha roi '
        elif N//100==4:
            out+= 'si roi '
        elif N//100==3:
            out+= 'sam roi '
        elif N//100==2:
            out+= 'song roi '
        elif N//100==1:
            out+='neung roi '
        N%=100
    if N>=10:
        if N//10==9:
            out+= 'kao sip '
        elif N//10==8:
            out+= 'paet sip '
        elif N//10==7:
            out+= 'chet sip '
        elif N//10==6:
            out+= 'hok sip '
        elif N//10==5:
            out+= 'ha sip '
        elif N//10==4:
            out+= 'si sip '
        elif N//10==3:
            out+= 'sam sip '
        elif N//10==2:
            out+= 'yi sip '
        elif N//10==1:
            out+='sip '
        N%=10
    if N>=0:
        if N == 9:
            out+='kao'            
        if N == 8:
            out+='paet'
        if N == 7:
            out+='chet'
        if N == 6:
            out+='hok'
        if N == 5:
            out+='ha'
        if N == 4:
            out+='si'
        if N == 3:
            out+='sam'
        if N == 2:
            out+='song'
        if N == 1:
            if len(t)>=2:
                out+='et'
            else:
                out+='neung'
        if N==0:
            if len(t)==1: 
                out+='soon'
    return out