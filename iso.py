pi=list(input())
p=[]
for i in pi:
    if i not in p:
        p.append(i)
if p==pi:
    print("Yes")
else:
    print("No")
        
