n = int(input())
winner = set()
loser = set()
for i in range(n):
    t = input().split()
    winner.add(t[0])
    loser.add(t[1])
print(sorted(winner-loser))
