
#
def how_many_cross(nlist : list, index : int):
    cnt = 0
    crossed_index_list = []
    for i, item in enumerate(nlist):
        if nlist[index][0] > item[0] and nlist[index][1] < item[1]:
            cnt += 1
            crossed_index_list.append(i)
        if nlist[index][0] < item[0] and nlist[index][1] > item[1]:
            cnt += 1
            crossed_index_list.append(i)
    return [cnt, crossed_index_list]

n = int(input())
nlist = []

for _ in range(n):
    nlist.append(list(map(int, input().split())))

#겹친 횟수 리스트 생성
cross_many_list = []
cross_index_list = []
for i in range(n):
    a = how_many_cross(nlist, i)
    cross_many_list.append(a[0])
    cross_index_list.append(a[1])

cnt = 0

while(True):
    print(cross_many_list)
    #겹치는 것이 없으면 종료
    if max(cross_many_list) == 0:
        break

    remove_index = cross_many_list.index(max(cross_many_list))
    cross_many_list[remove_index] = 0

    for num in cross_index_list[remove_index]:
        cross_many_list[num] -= 1

    cnt += 1

print(cnt)