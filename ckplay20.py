def mn_gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
def mn_lcm(x,y):
    lcm=(x*y)//mn_gcd(x,y)
    return lcm
m=list(map(int,input().split()))
print(mn_lcm(m[0],m[1]))
