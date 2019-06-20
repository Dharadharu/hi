n=int(input())
m=list(map(int,input().split()))
h=[]
for i in m:
    if m.count(i)>1:
        h.append(i)
    else:
        print(i)
    
