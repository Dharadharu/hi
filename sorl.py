ai=int(input())
a=list(map(str,input().split()))
a.sort(key=len)
print(*a)
