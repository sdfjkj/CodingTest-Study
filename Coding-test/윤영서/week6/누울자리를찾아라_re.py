import sys
input = sys.stdin.readline
N = int(input())
room = []
for i in range(N):
    room.append(input().rstrip())

g_count=0
s_count=0

# 가로
for i in range(N):
    count = 0
    for k in range(N):
        if room[i][k] == ".": #빈 공간이면 count+1
            count += 1
        else:
            if count >= 2:# 연속된 빈 공간이라면 g_count+1
                g_count += 1
            count = 0 #한줄 초기화
    if count >= 2:
        g_count += 1

# 세로
for i in range(N):
    count = 0
    for k in range(N):
        if room[k][i] == ".":
            count += 1
        else:
            if count >= 2:
                s_count += 1
            count = 0
    if count >= 2:
        s_count += 1

print(g_count, s_count)
