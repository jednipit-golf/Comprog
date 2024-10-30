n = input()
N = int(n)
K = 'K'
M = 'M'
B = 'B'
if N<1000:
    t = N
elif 1000<= N < 10000:
    t = str(round(N/1000,1))+'K'
elif 10000<= N < 1000000:
    t = str(int(round(N/1000,0)))+'K'
elif 1000000<= N < 10000000:
    t = str(round(N/1000000,1))+'M'
elif 10000000<= N < 100000000:
    t = str(int(round(N/1000000,1)))+'M'
elif 100000000<= N < 1000000000:
    t = str(int(round(N/1000000,0)))+'M'
elif 1000000000<= N < 10000000000:
    t = str(round(N/1000000000,1))+'B'
else:
    t = str(int(round(N/1000000000,0)))+'B'

print(t)
