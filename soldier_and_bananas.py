#https://codeforces.com/problemset/problem/546/A

i=input().split()
k,n,w=int(i[0]),int(i[1]),int(i[2])
r=int(k*(w*(w+1)/2))-n
print(r if r>0 else 0)
