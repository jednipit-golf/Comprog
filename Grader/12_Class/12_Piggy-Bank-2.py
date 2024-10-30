class piggybank:
    def __init__(self):
        self.coin = dict()
    def add(self, v, n):
        c = 0
        for i in self.coin:
            c += self.coin[i]
        if c+n > 100:
            return False
        else:
            if v not in self.coin:
                self.coin[v] = 0
            self.coin[v] += n
            return True
    def __float__(self):
        w = 0
        for i in self.coin:
            w += self.coin[i]*i
        return float(w)
    def __str__(self):
        n = ''
        a = sorted(self.coin)
        for i in a:
            n+= str(float(i))+':'+str(self.coin[i])+', '
        n = n[:-2:]
        n = '{'+n+'}'
        return n
 
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)