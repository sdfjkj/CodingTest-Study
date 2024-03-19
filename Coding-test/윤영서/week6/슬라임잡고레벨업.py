import sys
input = sys.stdin.readline

t=int(input())
d=[]
for i in range(t):
  k=int(input())
  d.append(k*(k+1)//2)

for i in d:
  l=1
  r=i
  while l<=r:
    n=(l+r)//2
    if i < n*(n+1) and i >=(n-1)*n:
      print(n)
      break
    elif i < n*(n+1):
      r=n-1
    else:
      l=n+1
