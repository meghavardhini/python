def  mn():
    nterms=5
    n1=1
    n2=1
    count=0
    while(count<nterms):
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
mn()
