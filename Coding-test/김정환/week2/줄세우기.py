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