import sys
#dfs
def dfs(idx):
    global visited
    visited[idx]=True
    print(idx, end=' ')
    for next in range(1,N+1):
        if graph[idx][next] and not visited[next]:
            dfs(next)

#bfs
def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1,N+1):
            if graph[cur][next] and not visited[next]:
                visited[next] = True
                q.append(next)


input = sys.stdin.readline
N,M,V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


dfs(V)
print()


visited = [False]*(N+1)
q=[V]
visited[V] = True
bfs()
