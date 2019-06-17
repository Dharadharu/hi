s=input()
c=0
for i in s:
    if ((i=='0') or (i=='1')):
        c=c+1
if (c==len(s)):
    print("yes")
else:
    print("no")
