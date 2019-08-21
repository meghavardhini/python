m,n=list(map(int,input().split()))
o,p=list(map(int,input().split()))
q,r=list(map(int,input().split()))
if(m==o==q) or (n==p==r) or (m==n and o==p and q==r):
    print("yes")
