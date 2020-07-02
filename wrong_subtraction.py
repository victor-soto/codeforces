#https://codeforces.com/problemset/problem/977/A
n,k=map(int,input().split())
while k > 0:
  n = n//10 if n%10 == 0 else n-1
  k-=1
print(n)
