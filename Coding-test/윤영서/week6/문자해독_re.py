import sys
input = sys.stdin.readline

g,S_len= map(int, input().split())
W = list(input().rstrip())
S = list(input().rstrip()) #AbrAcadAbRa

#찾는 문자열 W을 0,1 배열로 표현 / 알파벳 26*2 = 52
W_list = [0]*52
S_list = [0]*52
# ord(문자) : 유니코드 정수 반환 <-> chr(정수) : 정수에 해당하는 유니코드 문자 반환
for i in range(g):
    if 'a' <= W[i] <= 'z' :
        W_list[ord(W[i])-ord('a')]+=1
    else:
        W_list[ord(W[i])-ord('A')+26]+=1

# 이제 S를 g개 만큼 읽어가면서 배열이 같은지 확인할거임
# g개만큼 읽음을 나타내는 length
# 일치하는 배열의 수 count
# g개 중 처음 시작 값을 start

length = 0
count =0
start =0

# 문자열 S도 0,1 배열로 표현해서 비교하기 쉽게 만든다
for i in range(S_len):
    if 'a'<=S[i] <='z':
        S_list[ord(S[i])-ord('a')]+=1
    else:
        S_list[ord(S[i])-ord('A')+26]+=1
# 근데 숫자 배열로 바꾸는 동시에 비교도 같이 할거임
# 그래서 하나씩 바꾸면서 length+=1 하면서 g 길이랑 같아지면 멈추고 비교
    length+=1

    if length == g:
        if S_list==W_list:
            count+=1
        #같았던 같지 않았던 같에 다음거를 읽어주고 처음거 버릴거임
        #start =0 처음 값 버리기
        if 'a'<= S[start] <='z':
            S_list[ord(S[start])-ord('a')]-=1
        else:
            S_list[ord(S[start])-ord('A')+26]-=1
        #start 값 버렸으니까 그 다음 값이 start 값으로 바꾸고 길이도 하나 줄어듬
        start +=1
        length-=1
        #그 다음 length == g이 조건에 안 걸리니까 다시 length+=1하면서 그 다음 값 읽음

print(count)

# 윈도우 슬라이딩  Window Sliding
# 1. 찾는 문자열 -> 숫자 배열로
# 2. 긴 문자열도 숫자배열로 바꾸는데 정답, 길이, 시작점을 0으로 초기화하고 길이값 +=1하면서 읽음
# 3. 길이 값이 찾는 문자열 길이와 같으면 배열 비교하고 같으면 +=1
# 4. 같든 같지 않든 간 시작값을 숫자 배열로 바꾸는 같은 방법으로 -=1하고 시작값+=1, 길이-=1
# 5. 정답 값 출력 -> 그럼 자연스럽게 3. 조건문에 안 걸려서 2.으로 가면서 끝까지 읽는다
