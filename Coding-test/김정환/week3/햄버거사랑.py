n, m, t = map(int, input().split())

# n을 작은 수로 만들기
if n > m :
    n, m = m, n

burger = t // n
cola = t % n

# 콜라를 마시는 시간이 있을 때만 실행
if cola != 0:
    temp_burger = burger
    temp_cola = cola

    while temp_burger > 0:
        temp_burger -= 1
        temp_cola += n
        
        # 콜라 마시는 시간이 줄어든다면, 값을 변경
        if temp_cola % m < cola:
            burger = temp_burger + (temp_cola // m)
            cola = temp_cola % m

print(burger, cola)