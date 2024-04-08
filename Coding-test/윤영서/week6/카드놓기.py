import sys
from itertools import permutations
input = sys.stdin.readline

n= int(input())
k = int(input())
numbers = []
for i in range(n):
    h= int(input())
    numbers.append(h)
# print(numbers)
all_combinations = list(permutations(numbers,k))
all_strings = []
# print(all_combinations)
for i in range(len(all_combinations)):
    
    if k==2:
        combined_string=str(all_combinations[i][0])+str(all_combinations[i][1])
        all_strings.append(combined_string)
    elif k==3:
        combined_string=str(all_combinations[i][0])+str(all_combinations[i][1])+str(all_combinations[i][2])
        all_strings.append(combined_string)
    else:
        combined_string=str(all_combinations[i][0])+str(all_combinations[i][1])+str(all_combinations[i][2])+str(all_combinations[i][3])
        all_strings.append(combined_string)

answer = set(all_strings)
print(len(answer))