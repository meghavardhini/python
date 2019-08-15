def prime(n):              
    if n==1:
        return False
    elif n==2:
        return True
    else:
        c=0
        for i in range(2,n):
            if n%i==0:
                c=1
                break
        if c==0:
            return True
        else:
            return False

inp=int(input())         
f=[]
for h in range(2,inp+1):
    if prime(h):
        if inp%h==0:
            f.append(str(h))
print(" ".join(f))
