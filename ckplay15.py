m=list(input())
n=[]
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
for i in m:
    if i=='X':
        n.append("A")
    elif i=='Y':
        n.append("B")
    elif i=='Z':
        n.append("C")
    else:
        n.append(letters[letters.index(i)+3])
print("".join(n))
