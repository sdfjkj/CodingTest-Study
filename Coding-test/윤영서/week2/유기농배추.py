# 백준 1012번 BFS_deque (시간 : 173ms // 메모리 : 114148KB)
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(graph,a,b):
  d=deque()
  d.append((a,b))
  graph[a][b]=0
  while d:
    x,y = d.popleft()
    for i in range(4):
      nx = x+ dx[i]
      ny = y+ dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      elif graph[nx][ny]==1:
        graph[nx][ny]=0
        d.append((nx,ny))
  return 1
for i in range(t):
  count=0
  m, n, k = map(int, input().split())
  graph = [[0] * m for _ in range(n)]
  for j in range(k):
    a,b = map(int, input().split())
    graph[b][a]=1
  for a in range(n):
    for b in range(m):
      if graph[a][b]==1:
        bfs(graph,a,b)
        count+=1
  print(count)





