n=int(input())
lst=list(map(int,input().split()))[:n]
list1=lst[n//2]
list2=lst[n//2-1]
lost=list1+list2/2
print(lost)
