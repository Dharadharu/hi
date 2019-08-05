ai,bi=input().split()
ai=int(ai)
bi=int(bi)
l=[]
if(ai==1 and bi==1):
    print(1)
else:
    for i in range(2,bi):
        if(ai%i==0 and bi%i==0):
            l.append(i)
        else:
            continue
print(max(l))
