#https://www.acmicpc.net/problem/2343
import sys
# 각 블루레이에는 총 N개의 강의  M개의 블루레이
# 9 3
# 1 2 3 4 5/ 6 7 /8 9 => 15/13/17
input=sys.stdin.readline
N,M = map(int, input().split())
blu_ray = list(map(int, input().split()))
# print(blu_ray)
start=max(blu_ray) #각각 하나씩 담으면 최대 시간에 맞춰짐
end=sum(blu_ray) # 모두 하나에 담아버리기

while start <= end:
    mid = (start + end) // 2 

    #군집 개수 구하기
    total = 0
    count = 1
    for t in blu_ray:
        if total + t > mid: #mid 값이 넘지 않을 때까지 sum
            count += 1 #군집의 개수
            total = 0 #sum 값을 초기화
        total += t #mid 값이 넘지 않으면 계속 값 더하기


    if count <= M: #3개 이하의 군집일 경우 더 쪼개보기 
        ans = mid #현재 mid 값을 ans에 저장
        end = mid - 1 #더 쪼개기
    else:
        start = mid + 1#덜 쪼개기
    
print(ans)
