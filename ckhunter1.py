m=int(input())
n=[x for x in input().split()]
o=[]
for i in n:
    if n.count(i)>1:
        o.append(i)
if len(o)==0:
    print("unique")
else:
    print(' '.join(sorted(set(o))))
