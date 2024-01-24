n = int(input())
m = int(input())
nlist = list(map(int, input().split()))
nlist.sort(reverse=True)

start, end = 0, n-1
count = 0

while start<end:
    Sum = nlist[start] + nlist[end]
    if Sum > m:
            start += 1
    elif Sum < m:
         end -= 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)