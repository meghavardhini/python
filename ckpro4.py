a,b=map(str,input().split())
y=0
if len(a)>len(b):
    a,b=b,a
p=0
while p<len(a):
    y+=(ord(b[p])-ord(a[p]))
    p+=1
for p in range(p,len(b)):
    y+=ord(b[p])-ord('a')+1
print(y)
