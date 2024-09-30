import sys
input = sys.stdin.readline

H,W = map(int, input().split())
array = list(map(int, input().split()))

rain=0 

# print(array)
for i in range(1, W-1):
    left_max = max(array[:i])
    right_max = max(array[i+1:])
    k = min(left_max,right_max )
    if array[i] < k:
        rain+= k-array[i]
print(rain)