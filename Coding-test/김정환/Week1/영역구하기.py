m, n, k = map(int, input().split())
klist = [list(map(int, input().split())) for _ in range(k)]
map_list = [[0]*n for _ in range(m)]

print(klist)

for k in klist:
    for i in range(k[3]-k[1]):
        for j in range(k[2]-k[0]):
            map_list[k[1]+i][k[0]+j] = 1

print(map_list)

visit_list = map_list

x = 0
y = 0
count = 0
res = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]


