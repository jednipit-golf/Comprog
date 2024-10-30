bd,bm,by,d,m,y = [int(e) for e in input().split()]
m0 = 0;m1 = 31;m2 = 28;m3 = 31;m4 = 30;m5 = 31;m6 = 30;m7 = 31;m8 = 31;m9 = 30;m10 = 31;m11 = 30;m12 = 31
by = by-543
y = y-543
import math
if y-by >= 2:
    black = 365*((y-by)-1)
    if by%400 == 0 or (by%4 == 0 and by%100 != 0): #red ปีอธิกสุรธิน
        m2 = 29
        month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
        a = month[0:bm]
        red = 367-sum(a)-bd
        if y%400 == 0 or (y%4 == 0 and y%100 != 0):#blue ปีอธิกสุรธิน
            m2 = 29
            month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
            b = month[0:m]
            blue = sum(b)+d-1
        else:
            m2 = 28
            month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
            b = month[0:m]
            blue = sum(b)+d-1
    else:#red ปีธรรมดา
        m2 = 28
        month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
        a = month[0:bm]
        red = 366-sum(a)-bd
        if y%400 == 0 or (y%4 == 0 and y%100 != 0):#blue ปีอธิกสุรธิน
            m2 = 29
            month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
            b = month[0:m]
            blue = sum(b)+d-1
        else:
            m2 = 28
            month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
            b = month[0:m]
            blue = sum(b)+d-1
    X = red+ blue + black
else:
    if by%400 == 0 or (by%4 == 0 and by%100 != 0): #red ปีอธิกสุรธิน
        m2 = 29
        month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
        a = month[0:bm]
        red = 367-sum(a)-bd
        if y%400 == 0 or (y%4 == 0 and y%100 != 0):#blue ปีอธิกสุรธิน
            m2 = 29
            month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
            b = month[0:m]
            blue = sum(b)+d-1
        else:
            m2 = 28
            month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
            b = month[0:m]
            blue = sum(b)+d-1
    else:#red ปีธรรมดา
        m2 = 28
        month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
        a = month[0:bm]
        red = 366-sum(a)-bd
        if y%400 == 0 or (y%4 == 0 and y%100 != 0):#blue ปีอธิกสุรธิน
            m2 = 29
            month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
            b = month[0:m]
            blue = sum(b)+d-1
        else:
            m2 = 28
            month = [m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
            b = month[0:m]
            blue = sum(b)+d-1
    X = red+ blue
physical = round(math.sin((2*math.pi*X)/23),2)
emotional = round(math.sin((2*math.pi*X)/28),2)
intellectual = round(math.sin((2*math.pi*X)/33),2)
print(X,"{:.2f}".format(physical),"{:.2f}".format(emotional),"{:.2f}".format(intellectual))
    
        

 
     