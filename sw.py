ni=list(input())
y=len(ni)
for i in range(0,y,2):
    temp=ni[i]
    ni[i]=ni[i+1]
    ni[i+1]=temp
print("".join(ni))
