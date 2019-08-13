m,n=input().split()
if(len(m)!=len(n)):
    print("no")
else:
    v=[m.count(i) for i in m]
    p=[n.count(i) for i in n]
if(v==p):
    print("yes")
else:
    print("no")
