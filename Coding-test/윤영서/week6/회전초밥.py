import sys
from collections import deque
input = sys.stdin.readline

N,d,k,c = map(int, input().split())
arr =[int(input()) for i in range(N)]
#완벽한 한 바퀴를 위해 앞의 k-1개를 arr 배열 뒤에 추가
for i in range(k-1):
    arr.append(arr[i])
# print(arr)

start =0
length=0
d=deque()
count=[]

for i in range(len(arr)):
    length+=1
    d.append(arr[i])
    if length==k:
        co=len(set(d))
        if c in d:
            count.append(co)
        else:
            count.append(co+1)
        d.popleft()
        length-=1

print(max(count))
