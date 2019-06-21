ni,mi=list(map(int,input().split()))
s=[]
for i in range(1,100):
    if ni%i==0 and mi%i==0:
        s.append(i)
print(max(s))
        
