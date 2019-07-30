count=0
str=input()
for str1 in str:
    if(str1.isalpha() or str1.isdigit()):
        count+=1
if count!=0:
    print("yes")
else:
    print("no")
