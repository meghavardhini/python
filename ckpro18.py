m,n=map(int,input().split())
o=[]
p=0
for i in range(m):
    o.append(list(map(int,input().split())))   
for i in range(m):
    for j in range(n-1):
        for k in range(j+1,n+1):
            if o[i][j:k]==[1]*len(o[i][j:k]):
                 if all(o[p+i][j:k]==[1]*len(o[p+i][j:k]) for p in range(len(o[i][j:k])-1)):
                     if len(o[i][j:k])>p:
                        p=len(o[i][j:k])
if len(o)==1 and len(o[0])==1 and o[0][0]==1:
    print(1)
for i in range(p):
    print(*[1]*p) 

