n = int(input())
m = int(input())
nlist = list(map(int, input().split()))
nlist.sort()

res = 0
count = 1
index_a = 0
index_b = 1

## 좌 우에서 한칸 한칸씩 다가가고, 같은 인덱스면 스탑
## 그전에 매치되는 것이 있다면, 리스트에서 제거하고 다시 처음부터 

while(True):
    if index_a == n-1:
            break
    if nlist[index_a] + nlist[index_b] == m:
        res += 1
        index_a += 1
        index_b = index_a + 1
    elif nlist[index_a] + nlist[index_b] > m:
        index_a += 1
        index_b = index_a + 1
    else:
        index_b += 1

        if index_b == n:
            index_a += 1
            index_b = index_a + 1

print(res)