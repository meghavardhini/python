s,i=map(int,input().split())
list1=list(map(int,input().split()))
s=[]
list1.insert(0,0)
for y in range(i):
     vin=[]
     r=0
     bb,zz=map(int,input().split())
     for i in range(bb,zz+1):         
         r^=list1[i]     
     s.append(r)
for y in s:
     print(y)

