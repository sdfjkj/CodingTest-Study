# https://www.acmicpc.net/problem/13335
# 예시 답안은 나오지만 틀림 
import sys
input = sys.stdin.readline
n, w, L = map(int, input().split())
array = list(map(int, input().split()))

def solution(bridge_length, weight, truck_weights):
    time=0 # 최초 경과 시간 (0으로 설정)
    bridge = [0]*bridge_length  # bridge_length 길이만큼의 리스트(큐)

    currentWeight = 0 # 현재 다리 위의 무게를 저장하는 변수
    while len(truck_weights)>0:
        time+=1
        currentWeight = currentWeight - bridge.pop(0)

        if currentWeight+truck_weights[0] <= weight:
            currentWeight+=truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    time += bridge_length
    return(time)

print(solution(w, L, array))




# minTime=0
# sum=0
# temp_array=[]
# for i in range(n):
#     # 최대 무게를 버필 수 있고 w개수 값을 넘지 않는다면
#     if sum+array[i]<L and len(temp_array)<w and i!=n-1:
#         temp_array.append(array[i])
#         sum+=array[i]
#     elif sum+array[i]<L and len(temp_array)<w and i==n-1:
#         temp_array.append(array[i])
#         sum+=array[i]
#         minTime+=w
#     else:
#         minTime+=w+len(temp_array)
#         temp_array=[]

# print(minTime+1)