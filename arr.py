ai=list(map(int,input().split()))
bi=list(map(int,input().split()))
ci=list(map(int,input().split()))
l=[]
for i in range(len(ci)):
    bi.insert(i,ci[i])
    e=max(bi)
    l.append(e)
print(*l)
    
