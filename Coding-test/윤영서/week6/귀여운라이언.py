#https://www.acmicpc.net/problem/15565
import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int, input().split())
arr = list(map(int, input().split()))

length=0
indexarray=deque()
answer=deque()
for i in range(N):
    if arr[i]==1:
        length+=1
        indexarray.append(i)
        if length==K:
            answer.append(indexarray[2]-indexarray[0]+1)
            length-=1
            indexarray.popleft()
# print(answer)
print(-1) if not answer else print(min(answer))

