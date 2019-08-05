ai=list(map(int,input().split()))
bi=list(map(int,input().split()))
ci=list(map(int,input().split()))
if (ai[0]==bi[0]==ci[0]) or (ai[1]==bi[1]==ci[1]) or (ai[0]==ai[1] and bi[0]==bi[1] and ci[0]==ci[1]):
    print("yes")
else:
    print("no")

