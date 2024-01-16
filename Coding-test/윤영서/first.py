def Wee(x):
    # Wee의 내용
    
    def Coo(y):
        # Coo의 내용
        result = y **2  # 예시로 내부매개변수에 5를 더하는 연산을 수행
        print(result)
        return result
        
    
    result2 = x + 1  # Wee에서의 연산
    x = Coo(result2)  # Coo 호출
    
    return x

# Wee 호출
answer = Wee(5)
print(answer)