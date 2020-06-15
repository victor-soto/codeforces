#https://codeforces.com/problemset/problem/112/A
first, second = input(), input()
if first.lower() == second.lower():
  print(0)
else:
  first, second = first.lower(), second.lower()
  pos = next((i for i in range(len(first)) if first[i].lower() != second[i].lower()) , None)
  print(-1 if ord(first[pos]) < ord(second[pos]) else 1)
