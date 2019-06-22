import math
v,n=map(int,input().split())
w=(math.gcd(v,n))
print((v*n)//w)
