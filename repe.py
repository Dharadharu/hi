si=input()
s=0
for i in si:
    if si.count(i)>s:
        s=si.count(i)
        max=i
print(max)
