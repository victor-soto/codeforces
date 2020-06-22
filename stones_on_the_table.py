#https://codeforces.com/problemset/problem/266/A

n=int(input())
s=input()
replacements = 0
pivot = s[0]
for i in range(1,len(s)):
  if pivot == s[i]:
    replacements += 1
  else:
    pivot = s[i]
print(replacements)
