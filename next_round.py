#https://codeforces.com/problemset/problem/158/A

def inlt():
    return(list(map(int,input().split())))

n = inlt()
participants = inlt()

print(len([x for x in participants if x >= participants[n[1]-1] and x > 0]))