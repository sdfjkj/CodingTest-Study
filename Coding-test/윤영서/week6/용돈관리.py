import sys
input = sys.stdin.readline

N,M = map(int, input().split())
# data=[]
# for i in range(n):
#   data.append(int(input()))
data = [int(input()) for _ in range(N)]
# 최대와 최소를 구해야 함 
# > 최대는 돈 한번에 다 꺼냄. 
# 어느 경우라도 인출할 수 있는 최소의 금액은 행렬의 최솟값
l,r=  min(data), sum(data)

while l<=r:
  m=(l+r)//2
  now=m
  draw =1

  for i in data:
    if now < i:
      now=m
      draw+=1
    now-=i

  if draw > M or m< max(data):
    l=m+1
  else:
    r=m-1
    k=m
print(m)
