m=int(input(""))
n=list(map(int,input().split()))
max=0
min=0
if(m==1):
    min=1
    print(min)
else:
    for i in range(0,len(n),1):
        o=n.count(i)
        if(o==1):
            min+=1
            print(min)
            break
