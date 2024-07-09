# https://www.acmicpc.net/problem/12868
# 해결못함
def find_string(n, v, s):
  """
  문자열 S보다 사전순으로 앞서지 않으면서 인버스 갯수가 V 이상인 문자열 R을 찾는다.
  
  Args:
      n: 문자열 길이 (1 ≤ N ≤ 20)
      v: 필요한 최소 인버스 갯수 (0 ≤ V ≤ N×(N-1)/2)
      s: 원본 문자열 (알파벳 소문자 처음 N개로 구성됨, 중복 없음)
  
  Returns:
      조건을 만족하는 문자열 R 또는 -1 (문자열이 없는 경우)
  """

  # 사용 가능한 알파벳 목록 (정렬된 문자열로 초기화)
  available_chars = "".join(chr(i) for i in range(ord('a'), ord('a') + n))

  # 문자열 S의 인버스 갯수 계산
  inversions = 0
  for i in range(n - 1):
    for j in range(i + 1, n):
      if s[i] > s[j]:
        inversions += 1

  # 필요한 추가 인버스 갯수 계산
  required_inversions = v - inversions

  # 사전순으로 가장 앞서는 문자열 R 구성
  r = []
  for i in range(required_inversions):
    # 사용 가능한 알파벳 중에서 S[i]보다 큰 첫 번째 문자 선택
    index = available_chars.find(str(s[i] + 1))
    if index == -1:
      # S[i]보다 큰 문자가 없으면 다음 문자로 이동
      index = available_chars.find(f"{s[i] + 1}")
    r.append(available_chars[index])
    available_chars = available_chars[:index] + available_chars[index + 1:]

  # 남은 문자열 구성
  r += available_chars

  # 문자열 S보다 사전순으로 앞서는지 확인
  if s[0] > r[0]:
    return -1

  return "".join(r)

# 입력 받기
n = int(input())
v = int(input())
s = input()

# 문자열 찾기
result = find_string(n, v, s)

# 결과 출력
if result == -1:
  print(-1)
else:
  print(result)
