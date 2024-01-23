com = int(input())
line = int(input())
web = set()

line_list = [list(map(int, input().split())) for _ in range(line)]

for line in line_list:
    if line[0] == 1 or line[1] == 1:
        web.add(line[0])
        web.add(line[1])

for _ in range(com):
    for line in line_list:
        if line[0] in web or line[1] in web:
            web.add(line[0])
            web.add(line[1])

if len(web) == 0:
    print(0)
else:
    print(len(web)-1)

    # 실험