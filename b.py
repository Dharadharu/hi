a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
for i in range(0,len(c)):
        
    if b in c:
        print("yes")
        break;
else:
    print("no")

