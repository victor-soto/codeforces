#https://codeforces.com/problemset/problem/231/A
import sys
input = sys.stdin.readline

def inp():
  return(int(input()))

def read_lines(n):
  return [sys.stdin.readline().strip() for _ in range(n)]

n = inp()
lines = read_lines(n)
total = 0

for line in lines:
  if len([x for x in line.split() if x == '1']) > 1:
    total += 1

print(total)