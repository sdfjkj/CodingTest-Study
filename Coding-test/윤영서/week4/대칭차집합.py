#https://www.acmicpc.net/problem/1269
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr1 = list(map(int, input().split()))
# print(arr1)
arr2 = list(map(int, input().split()))
# print(arr2)
print(len(list(set(arr1)-set(arr2)))+len(list(set(arr2)-set(arr1))))
# print(len(arr1) + len(arr2)-count*2)
