def total(pocket):
    t = 0
    for i in pocket.keys():
        t += i * pocket[i]
    return t
def take(pocket, money_in):
    for i in money_in.keys():
        if i in pocket:
            pocket[i] = pocket[i] + money_in[i]
        else:
            pocket[i] = money_in[i]


def pay(pocket, amt):
    money_out = {}
    for m in sorted(pocket.keys())[::-1]:
        if amt >= m:
            c = min(pocket[m], amt//m)
            money_out[m] = c
            poxket[m] -= c
            amt -= m*c
    if amt > 0:
        take(pocket, money_out)
        money_out = {}
        return money_out 
    elif amt == 0:
        return money_out 
        

exec(input().strip())