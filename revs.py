ni=int(input())
si=list(input())
h=[]
c=0
for i in range(len(si)):
    if (si[i]=='a' or si[i]=='e' or si[i]=='i' or si[i]=='o' or si[i]=='u'):
        c=c+1
    else:
        h.append(si[i])
n=h[::-1]
print(''.join(n))
