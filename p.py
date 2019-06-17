s=int(input())
if s==2:
    print("yes")
elif s>1:
    for i in range(2,s):
        if(s%i)==0:
            print("no")
            break;
    else:
        print("yes")
