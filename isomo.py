ai,bi=map(str,input().split())
if len(ai)!=len(bi):
    print("no")
n1=[ai.count(i) for i in ai]
n2=[bi.count(i) for i in bi]
if (n1==n2):
    print("yes")
else:
    print("no")
    
