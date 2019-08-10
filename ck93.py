m=input()
n=[]
for i in m:
    if(i.isnumeric()):
        n.append(i)
print(''.join(n))
