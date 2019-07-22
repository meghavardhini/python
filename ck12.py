def mn():
    n=int(input("enter the no:"))
    sum=n
    r=0
    while(n>0):
        i=n%10
        r=r*10+i
        n=n//10
    if(sum==r):
        print("yes")
    else:
        print("no")
mn()
    
