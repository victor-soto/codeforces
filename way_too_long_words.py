#https://codeforces.com/problemset/problem/71/A
import sys
input = sys.stdin.readline

def inp():
  return(int(input()))

def read_lines(n):
  return [sys.stdin.readline().strip() for _ in range(n)]

n = inp()
lines = read_lines(n)
formatted_lines = []
for line in lines:
  formatted_lines.append(line[0] + str(len(line[1:len(line)-2])+1) + line[len(line)-1] if len(line) > 10 else line)
print(*formatted_lines, sep = "\n")