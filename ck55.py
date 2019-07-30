i=0
sum=0
x=int(input())
while(x>0):
    r=x%10
    sum=sum+r
    x=x//10
print(sum)
