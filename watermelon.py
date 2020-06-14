# https://codeforces.com/problemset/problem/4/A
import sys
input = sys.stdin.readline

def inp():
  return(int(input()))

n = inp()
even_numbers = [i for i in range(2,n) if i%2==0]
print('YES' if any(even_numbers) and n%2 == 0 else 'NO')