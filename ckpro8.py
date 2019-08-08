import math
m,n=map(int,input().split())
o=[]
p=list(map(int,input().split()))
for i in range(0,n):
    q,r=map(int,input().split())
    o.append([q,r])
for i in o:
    s1=i[0]-1
    s2=i[1]-1
    print(math.gcd(p[s1],p[s2]))
