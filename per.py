p,q=map(int,input().split())
r=p*q
for i in range(0,r+1):
    if i**2==r:
        print("yes")
        break;
else:
    print("no")
    
