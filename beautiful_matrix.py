#https://codeforces.com/problemset/problem/263/A
import sys

def read_lines(n):
  return [sys.stdin.readline().strip() for _ in range(n)]

lines = read_lines(5)
positions = [(index, row.index('1')) for index, row in enumerate([x.split() for x in lines]) if '1' in row]
print(abs(2-positions[0][0]) + abs(2-positions[0][1]))
