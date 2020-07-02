#https://codeforces.com/problemset/problem/791/A
n=input().split()
a,b=int(n[0]),int(n[1])
c=0
while a<=b:
  a*=3
  b*=2
  c+=1
print(c)
