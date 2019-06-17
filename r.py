p=int(input())
r,s=input().split()
r=int(r)
s=int(s)
if p in range(r+1,s):
    print("yes")
else:
    print("no")
