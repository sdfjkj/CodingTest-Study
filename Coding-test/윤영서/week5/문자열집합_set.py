#https://www.acmicpc.net/problem/14425 - 통과
# 메모리 116008KB / 시간 312ms
from itertools import count # 쓰면 메모리 116004KB / 시간 272ms
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s=set()
count=0

for _ in range(n):
  data = input().rstrip()
  s.add(data)

for _ in range(m):
  data= input().rstrip()
  if data in s:
    count+=1
print(count)
