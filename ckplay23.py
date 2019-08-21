m,n=map(int,input().split())
y=min(m,n)
x=[]
for i in range(1,y+1):
    if((m%i==0) and (n%i==0)):
        x.append(i)
print(max(x))
