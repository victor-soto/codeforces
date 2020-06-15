#https://codeforces.com/problemset/problem/282/A
total = 0

for _ in [0]*int(input()):
  total = total + (1 if '++' in input() else -1)

print(total)