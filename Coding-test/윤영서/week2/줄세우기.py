# 메모리 114024KB // 시간 : 208ms
# import sys
# t=int(sys.stdin.readline())
# count=0

# for k in range(1,t+1):
#   data = list(map(int, input().split()))
#   count=0
#   for i in range(1,len(data)-1):
#     for j in range(i+1, len(data)):
#       if data[i] > data[j]:
#         data[i],data[j] = data[j],data[i]
#         count+=1
#   print(data[0], count)

# 메모리 114024KB // 시간 : 168ms
from collections import deque

testcases = int(input())
res_list = []

for testcase in range(testcases):

    nlist = list(map(int, input().split(' ')))

    n = nlist[0]
    nque = deque(nlist[1:])
    newlist = []
    res = 0

    while(nque):
        temp = nque.popleft()
        newlist.append(temp)
        newlist.sort()
        a = newlist.index(temp)
        res += len(newlist) -1 -a

    res_list.append(res)

for a,b in enumerate(res_list):
    print(f"{a+1} {b}")