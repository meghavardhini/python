a,b=map(int,input().split())
c=map(int,input().split())
d=[]
for p in c:
    if(int(p)%2!=0):
        d.append(p)
print(d[b-1])


