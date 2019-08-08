sr=input()
t=[]
flag=0
a=list=['aeiouAEIOU']
for i in sr:
    if i in a:
        print("yes")
        flag=1
        break
if flag==0:
    print("no")
