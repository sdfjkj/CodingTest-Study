#https://www.acmicpc.net/problem/14425 - 통과
# 메모리 117360KB / 시간 272ms
from itertools import count 
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d={}
count=0

for _ in range(n):
  data = input()
  d[data] = True

for _ in range(m):
  data= input()
  if data in d:
    count+=1

print(count)
