#https://codeforces.com/problemset/problem/116/A
import sys
input = sys.stdin.readline

def inp():
  return(int(input()))

def read_lines(n):
  return [sys.stdin.readline().strip() for _ in range(n)]

n=inp()
lines=read_lines(n)
stops=[]
for i in range(n):
  a,b=map(int,lines[i].split())
  if len(stops):
    stops.append(stops[i-1]-a+b)
  else:
    stops.append(b)
print(max(stops))