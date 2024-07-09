import sys
from collections import deque
answer=[]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
q=deque()
count=1
#bfs 함수
def bfs(x,y):
    global q, count
    q.append([x,y])
    graph[x][y]=0
    while q:
        ax,ay = q.popleft()
        for i in range(4):
            cx=ax+dx[i]
            cy=ay+dy[i]
            if cx>=0 and cx<N and cy>=0 and cy<N and graph[cx][cy]==1:
                graph[cx][cy]=0 #visited 으로 바꿈
                q.append([cx,cy])
                count+=1
    answer.append(count)

#그래프 그리기
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    array = list(map(int, input().rstrip()))
    graph.append(array)
# print(graph)


#처음 1인 부분 찾기
#dfs(첫 1좌표)
for i in range(N):
    for m in range(N):
        if graph[i][m]==1:
            count=1
            bfs(i,m)

print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])

