n=input()
count=0
c=0
for i in range(0,len(n)):
    if n[i].isdigit() or n[i].isalpha() or n[i]==" ":
        c=c+1
    else:
        count+=1
print(count)

