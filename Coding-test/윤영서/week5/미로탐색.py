# https://www.acmicpc.net/problem/2178
# 메모리 : 114148KB/ 시간 : 148ms
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a=[]
for _ in range(n):
  a.append(list(map(int, input().rstrip())))
# print(a)
count=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x,y):
  q=deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=ny and ny<=m-1 and 0<=nx and nx<=n-1 and a[nx][ny]==1 :
        q.append((nx,ny))
        a[nx][ny] = a[x][y]+1
  return a[n-1][m-1]

print(bfs(0,0))