m=(input())
n=str(input())
o=('a','e','i','o','u')
for i in n:
    if i in o:
        n=n.replace(i,"")
print(n[::-1])
    

