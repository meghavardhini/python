def mn():
    x=int(input("enter the nos:"))
    count=0
    while(x>0):
        x=x//10
        count=count+1
    print(count)
mn()
