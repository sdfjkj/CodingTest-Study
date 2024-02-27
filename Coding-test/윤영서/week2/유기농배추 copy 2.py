# 백준 1012번 DFS_재귀 (Recursion Error))
import sys
sys.setrecursionlimit(3000) # 시간 : 256ms //  메모리 : 311704KB
input = sys.stdin.readline
t = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(a,b):
  for i in range(4):
    nx = a+dx[i]
    ny = b+dy[i]
    if nx>=0 and nx<n and ny>=0 and ny <m:
      if graph[nx][ny] ==1:
        graph[nx][ny]=0
        print("=>",nx, ny)
        dfs(nx,ny)
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
        dfs(a,b)
        count+=1
  print(count)