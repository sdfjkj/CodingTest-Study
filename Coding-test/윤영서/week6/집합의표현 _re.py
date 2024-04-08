import sys
sys.setrecursionlimit(100000)
sys.setrecursionlimit(10000)
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
parents = [0] *(n+1)

for i in range(n+1):
    parents[i] =i

def find(a): #최상위 조상 찾기
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a,b): #합칠 때 바로 위 조상값으로 바꾸기
    a=find(a)
    b=find(b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b

for _ in range(m):
    i,a,b = map(int, input().split())
    if i==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print("yes")
        else:
            print("no")
