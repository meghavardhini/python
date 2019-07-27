n=int(input())
lst=list(map(int,input().split()))[:n]
lst.sort()
print(*lst,end=" ")
