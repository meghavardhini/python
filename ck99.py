p,q,r=map(int,input().split())
s=0
for i in range(0,r):
    s=s+p
    p=p+q
print(s)
