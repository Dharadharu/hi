sl=input()
si=list(map(int,input().split()))
s=1
for i in si:
    if si.count(i)==s:
        print(i)
        break;
    else:
        continue;
