def mn():
    num=371
    sum=0
    temp=num
    while(temp>0):
        r=temp%10
        sum=sum+(r*r*r)
        temp=temp//10
    if (sum==temp):
            print("nt a armstorng no")
    else:
            print("amstrong no")
mn()
