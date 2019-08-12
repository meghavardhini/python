b=input()
yak=map(int,input().split())
s=[]
for i in yak:
    eat=bin(i)
    s.append(eat)
fine=sorted(s)
fine.reverse()
for j in fine:
    print(int(j,2))


