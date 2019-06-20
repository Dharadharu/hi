n=int(input())
m=list(map(int,input().split()))
h=[]
for i in range(n):
    if i==m[i]:
        h.append(m[i])
h.sort()
if len(h)==0:
    print("-1")
else:
    print(*h)
