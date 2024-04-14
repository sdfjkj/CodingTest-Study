# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3
import sys
from collections import deque
input = sys.stdin.readline
s=list(input().rstrip())
print(s)
n=1 #압축 단위
compressed_len = []
while True:
    if n>len(s)//2:
        break
    else:
        # 압축 단위만큼 자르고 압축된 길이를 배열이 추가
        # n++
        window = deque(s[:n])
        # print(window)
        answer = window
        k=len(s)
        for i in range(n,len(s)):
            for k in range(n):
                answer.popleft()
                answer.append(i)
            if answer==window:
                k=k-n+2
            else:
                window.popleft()
                window.append(i)
            # answer = max(len(answer), len(window))
        compressed_len.append(k)
        n=n+1
# print(min(compressed_len))
print(compressed_len)