m=input()
m=list(m)
n=""
for i in range(0,len(m)-1,2):
    temp=m[i+1]
    m[i+1]=m[i]
    m[i]=temp
print(n.join(m))
