from collections import Counter     
string="kabali"
m=int(input())
n=[]
count=0
if m>=1 and m<=1000:
    for i in range(m):
        n.append(input())
for j in n:
        if Counter(j)==Counter(string):
            count=count+1
print(count)
