m=int(input())
n=list(map(int,input().split()))
y=[1]*m
for i in range(m):
    if i==0:
        if n[i]>n[i+1]:
            y[i]=y[i]+y[i+1]
    elif i>0:
        if n[i]>n[i-1]:
            y[i]=y[i]+y[i-1]
print(sum(y))
        
