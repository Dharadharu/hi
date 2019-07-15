li,ri=map(int,input().split())
h=[]
for i in range(li,ri+1):
    if(i%li==0 and i%ri==0):
        h.append(i)
    else:
        print(li*ri)
        break;
h.sort()
print(max(h))
