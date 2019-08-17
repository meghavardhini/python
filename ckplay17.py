m=input()
n=0
for i in m:
    if m.count(i)>n:
        n=m.count(i)
        o=i
print(o)
