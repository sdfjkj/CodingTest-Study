
#
def how_many_cross(nlist : list, index : int):
    cnt = 0
    for i, item in enumerate(nlist):
        if nlist[index][0] > item[0] and nlist[index][1] < item[1]:
            cnt += 1
        if nlist[index][0] < item[0] and nlist[index][1] > item[1]:
            cnt += 1
    return cnt

n = int(input())
nlist = []
cnt = 0

for _ in range(n):
    nlist.append(list(map(int, input().split())))

while(True):
    max_list = []
    #가장 많이 겹치는 전깃줄 반환
    for i in range(len(nlist)):
        max_list.append(how_many_cross(nlist, i))

    if max(max_list) == 0:
        break
    print('지우기전 리스트 :', nlist)
    print('지우기전 겹치는 값 :',max_list)

    a = max_list.index(max(max_list))
    del max_list[a]
    del nlist[a]
    cnt += 1

    max_list = []

    for i in range(len(nlist)):
        max_list.append(how_many_cross(nlist, i))

    print('지운 후 리스트 :',nlist)
    print('지운 후 값 :',max_list)
    print(cnt)
    print()
    print()

print(cnt)