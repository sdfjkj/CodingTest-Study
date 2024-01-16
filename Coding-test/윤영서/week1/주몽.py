import sys
n= int(sys.stdin.readline())
m= int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
count=0
for i in data:
    if m-i in data:
        count+=1

print(count//2)
