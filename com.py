m=int(input())
if m==1:
    print("no")
elif(m>1):
    for i in range(2,m):
        if m%i==0:
            print("yes")
            break;
    else:
        print("no")
else:
    print("no")
    
