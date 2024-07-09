# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
input = sys.stdin.readline
deque = deque()
N,M,V = map(int, input().split())
# print(N,M,V)
graph = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# print(graph)    

#dfs
visited = [0]*(N+1)
def dfs(V, visited):
    visited[V]=1
    print(V, end=' ')
    for w in range(1,N+1):
        if graph[V][w]==1 and visited[w]==0:
            dfs(w,visited)


#bfs
def bfs(V):
    bfs_list = [V]
    print(V, end=' ')
    deque.append(V)
    while deque :
        v = deque.popleft()
        for w in range(1,N+1):
            if w not in bfs_list and graph[v][w]:
                deque.append(w)
                print(w, end=' ')
                bfs_list.append(w)
        


print(dfs(V, visited))
print(bfs(V))
##실패 -> 형식이 틀린 듯 []이런 배열
# [3, 1, 2, 5, 4]
# [3, 1, 4, 2, 5]
# 내 답은 이런식인데 예제 출력은 
# 3 1 2 5 4
# 3 1 4 2 5
# 배열이 아닌 형태 답의 형식을 바꾸기 보다는 처음부터 출려되는 함수 내부에서 수정해야할 듯
# 3 1 2 5 4 None
# 3 1 4 2 5 None