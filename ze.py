n=int(input())
m=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
        if m[i]+m[j]==0:
            print(m[i],m[j])
        
