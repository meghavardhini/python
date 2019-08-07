c=int(input())
h=[]
i=0
for j in range(0,c+1):
    i=abs((2**j)-c)
    h.append(i)
k=min(h)
print(k)
