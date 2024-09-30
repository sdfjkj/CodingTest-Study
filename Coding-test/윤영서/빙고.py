import sys
input = sys.stdin.readline
def bingoCount(graph):
    bingo=0
    sum=0
    for j in range(5):
        if array[j][0]==0 and array[j][1]==0 and array[j][2]==0 and array[j][3]==0 and array[j][4]==0 :
                    bingo+=1
        # for k in range(5):
        #     sum+=graph[j][k]
        #     if k==4:
        #         if sum==0:
        #             bingo+=1
        #         sum=0
    for k in range(5):
        if array[0][k]==0 and array[1][k]==0 and array[2][k]==0 and array[3][k]==0 and array[4][k]==0 :
                bingo+=1
        # for k in range(5):
        #     sum+=graph[k][j]
        #     if k==4:
        #         if sum==0:
        #             bingo+=1
        #         sum=0
    if array[0][0]==0 and array[1][1]==0 and array[2][2]==0 and array[3][3]==0 and array[4][4]==0 :
        bingo+=1
    if array[4][0]==0 and array[3][1]==0 and array[2][2]==0 and array[1][3]==0 and array[0][4]==0 :
        bingo+=1
    return bingo
#bingo의 개수를 return


array = [(list(map(int, input().split()))) for _ in range(5)]
# graph = [[0]*5 for _ in range(5)]
# array=[]
# for i in range(5):
#     a = list(map(int, input().split()))
#     array.append(a)
# print(array)
# print(graph)
count =0
bingo=0
for i in range(5):
    num = list(map(int, input().split()))
    for i in num:
        # print(i)
        for j in range(5):
            for k in range(5):
                if i==array[j][k]:
                    array[j][k]=0
                    count+=1
                    #값을 하나씩 부를 때마다 bingo 개수 세는 함수에 그래프 넣기
                    if bingoCount(array)==3:
                        # print("count!!!!!!!!!!!!!!!!!!!",count)
                        print(count)
                        array=[[100]*5 for _ in range(5)]
                        break
                        
                    #array[j][k]가 포함된 줄 값이 모두 0이면 bingo+=1 
                    #대각선인 경우 (00,11,22,33,44)
                    # if j==k :
                    #     if array[0][0]==0 and array[1][1]==0 and array[2][2]==0 and array[3][3]==0 and array[4][4]==0 :
                    #         bingo+=1
                    # if j+k==4:
                    #     if array[4][0]==0 and array[3][1]==0 and array[2][2]==0 and array[1][3]==0 and array[0][4]==0 :
                    #         bingo+=1
                    # else:
                    #     if array[j][0]==0 and array[j][1]==0 and array[j][2]==0 and array[j][3]==0 and array[j][4]==0 :
                    #         bingo+=1
                    #     if array[0][k]==0 and array[1][k]==0 and array[2][k]==0 and array[3][k]==0 and array[4][k]==0 :
                    #         bingo+=1
                    #bingo가 3이면 count값 출력하고 break
                    
# for i in array:
#     for k in i:
#         print(k)