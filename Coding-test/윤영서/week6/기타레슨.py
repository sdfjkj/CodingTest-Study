# #https://www.acmicpc.net/problem/2343
# import sys
# # 각 블루레이에는 총 N개의 강의  M개의 블루레이
# # 9 3
# # 1 2 3 4 5/ 6 7 /8 9 => 15/13/17
# input=sys.stdin.readline
# N,M = map(int, input().split())
# blu_ray = list(map(int, input().split()))
# # print(blu_ray)
# start=max(blu_ray) #각각 하나씩 담으면 최대 시간에 맞춰짐
# end=sum(blu_ray) # 모두 하나에 담아버리기

# while start <= end:
#     mid = (start + end) // 2 

#     total = 0
#     count = 1
#     for t in blu_ray:
#         if total + t > mid:
#             count += 1
#             total = 0
#         total += t 

#     if count <= M:
#         ans = mid
#         end = mid - 1
#     else:
#         start = mid + 1
    
# print(ans)
# print(count)