import sys

# n = 학교 수, m = 노드 수
n, m = map(int, input().split())

MW_list = list(map(str, input().split()))

# 부모 테이블 초기화
parent = [0] * (n+1)


for i in range(1, n+1):
    parent[i] = i

# 부모 노드를 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# a, b의 부모 노드 찾아서 하나의 부모 노드로
def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b

# 간선 정보를 리스트에 담고, 낮은 비용을 기준으로 정렬
edges = []
total_cost = 0
cnt = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort

for i in range(m):
    cost, a, b = edges[i]

    # 남학교 <-> 여학교인 경우에만 길 연결
    if MW_list[a-1] != MW_list[b-1]:

        # a의 부모노드와 b의 부모노드가 다르다면 사이클을 생성하지 않음
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
            cnt += 1
            
print(cnt)
if cnt == n-1:
    print(total_cost)
else:
    print(-1)