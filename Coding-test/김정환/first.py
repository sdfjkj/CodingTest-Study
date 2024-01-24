## 좌 우에서 한칸 한칸씩 다가가고, 같은 인덱스면 스탑
## 그전에 매치되는 것이 있다면, 리스트에서 제거하고 다시 처음부터 

n = int(input())
m = int(input())
nlist = list(map(int, input().split()))

while(True):
    