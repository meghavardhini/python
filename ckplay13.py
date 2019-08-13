m,n=map(int,input().split())
o=list(map(int,input().split()))
for i in range(n):
    o=[o[-1]]+o[:-1]
print(*o,end=" ")
