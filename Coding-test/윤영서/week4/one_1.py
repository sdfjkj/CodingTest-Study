# https://www.acmicpc.net/problem/4375
import sys
input = sys.stdin.readline
while True:
  try:
    n= int(input())
  except:
    break
  num=1
  count=1
  while True:
    if num%n !=0:
      num = (num % n) * (10 % n) +1
      num %= n
      count+=1
    else:
      break
  print(count)