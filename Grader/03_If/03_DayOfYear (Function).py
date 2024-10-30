def day_of_year(d, m, y):
    dd = int(d)
    mm = int(m)
    yy = int(y)
    m0 = 0
    m1 = 31
    m2 = 28
    m3 = 31
    m4 = 30
    m5 = 31
    m6 = 30
    m7 = 31
    m8 = 31
    m9 = 30
    m10 = 31
    m11 = 30
    m12 = 31
    YY = yy-543
    if YY%400 == 0 or ( YY%4 == 0 and YY%100 !=0 ):
        m2 = 29
    month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
    u = month[0:m]
    number_of_date = dd+sum(u)
    return number_of_date
exec(input()) 