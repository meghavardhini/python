m=int(input())
n=[int(o) for o in input().split(" ")]
p=0
for q in range(m):
    for r in range(q):
        if(n[r]<n[q]):
            p+=n[r]
print(p)
