# https://www.acmicpc.net/problem/2606
from collections import deque
import sys
n=int(sys.stdin.readline())
connect = int(sys.stdin.readline())
graph = [[] for  i in range(n+1)]
visited = [False] * (n+1)
count=0

for i in range(connect):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

#print(graph)
def bfs(graph,v):
    global count
    queue = deque([v])

    while queue:
        pop = queue.popleft()
        visited[pop]=True
        for i in graph[pop]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                count+=1
    print(count)
bfs(graph,1)
