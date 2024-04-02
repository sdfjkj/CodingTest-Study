m = int(input())
nlist = []
test = set()
duplication = set()
res = 1
index = 0

#입력
for _ in range(6):
    line = list(map(int, input().split()))
    nlist.append(line)

#중복확인
for line in nlist:
    if line[0] in test:
        duplication.add(line[0])
    else:
        test.add(line[0])

test = test - duplication

print(test)
print(nlist)

#전체 넓이 구하기
for line in nlist:
    if line[0] in test:
        res = res * line[1]
        index = nlist.index(line)

print(index)

#제거할 영역 구하기
res -= nlist[(index+2) % 6][1] * nlist[(index+3) % 6][1]

print(res*m)