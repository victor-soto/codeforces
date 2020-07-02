#https://codeforces.com/problemset/problem/617/A
n=int(input())
print(n//5 + (0 if n%5==0 else 1))
