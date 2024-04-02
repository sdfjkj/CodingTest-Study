import sys
input = sys.stdin.readline

n,k = map(int, input().split())
d=[[0,0]]
pack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
  d.append(list(map(int, input().split())))

for i in range(1,n+1):
  for j in range(1,k+1):
    weight = d[i][0]
    val = d[i][1]
    if j <weight:
      pack[i][j] = pack[i-1][j]
    else:
      pack[i][j] = max(val+pack[i-1][j-weight], pack[i-1][j])

print(pack[n][k])