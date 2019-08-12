m,n=map(int,input().split())
o=list(map(int,input().split()))
l1=[]
for i in range(0,n):
     a,b=map(int,input().split())
     l1.append([a,b])
for i in range(n):
     lower=l1[i][0]
     upper=l1[i][1]
     x=sum(o[lower-1:upper])
     print(x)
