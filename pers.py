import math
ai,bi=input().split()
ai=int(ai)
bi=int(bi)
count=0
for i in range(ai,bi+1):
    j=int(math.sqrt(i))
    if(i==j*j):
        count=count+1
    else:
        continue
print(count)
        
    
