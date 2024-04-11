import sys
input = sys.stdin.readline
t = int(input())
from collections import deque

def min_ances(graph,k):
  answer=[k]
  a=deque()
  a.append(k)
  while a:
    i = a.popleft()
    for k in range(n):
      if graph[k][i]==1:
        a.append(k)
        answer.append(k)
  return answer
    
for _ in range(t):
  n = int(input())
  graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
  for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a][b] = 1
  s1,s2 = map(int, input().split())
  # print(graph)
  a1=min_ances(graph,s1)
  a2 = min_ances(graph,s2)
  print(a1)
  print(a2)
  k=list(set(a1)&set(a2))
  print(k)
  print(k[len(k)-1])
  #set 순서가 보장되지 않음
  #메모리 초과






