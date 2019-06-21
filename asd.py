ni=int(input())
m=list(map(int,input().split()))
for i in m:
    if m[i]>m[i+1]:
        print(i)
        break;
