# https://www.acmicpc.net/problem/1181
import sys
input = sys.stdin.readline
N = int(input())
array=[]
# array = [(input().rstrip()) for _ in range(N)]
length_array = [[]*N for _ in range(60)]

for _ in range(N):
    word = (input().rstrip())
    # print(word, len(word))
    length_array[len(word)].append(word)
# print(array)
# print("length_array",length_array)
# length_array.sort()
for i in range(60):
    if length_array[i] !=[]:
        if len(length_array[i])==1:
            print(length_array[i][0])
        else:
            # print("length_array", sorted(set(length_array[i])))
            new = sorted(set(length_array[i]))
            for i in new:
                print(i)
            
