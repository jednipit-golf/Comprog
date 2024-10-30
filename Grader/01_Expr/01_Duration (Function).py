def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + \
    ('0'+str(m))[-2:] + ':' + \
    ('0'+str(s))[-2:]
def to_sec(h,m,s):
    x = h*3600+m*60+s
    return x

def to_hms(S):
    HH = S//3600
    d0 = S%3600
    MM = d0//60
    d1 = d0%60
    SS = d1
    return HH,MM,SS

def diff(h1,m1,s1,h2,m2,s2):
    t1 = h1*3600 + m1*60 + s1
    t2 = h2*3600 + m2*60 + s2
    dt = t2-t1
    HH = dt//3600
    d0 = dt%3600
    MM = d0//60
    SS = d0%60
    return HH,MM,SS
def main():
    hms_start = input()
    hms_end = input()
    h1,m1,s1 = str2hms(hms_start)
    h2,m2,s2 = str2hms(hms_end)
    h,m,s = diff(h1,m1,s1,h2,m2,s2)
    x = hms2str(h,m,s)
    print(x)
exec(input())