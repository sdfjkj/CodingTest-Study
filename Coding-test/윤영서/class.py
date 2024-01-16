class MyClass:
    def Wee(self, x):
        # Wee의 내용

        def Coo(y):
            # Coo의 내용
            result = y ** 2  # 예시로 내부매개변수에 5를 더하는 연산을 수행
            print(result)
            return result

        result2 = x + 1  # Wee에서의 연산
        x = self.Coo(result2)  # Coo 호출

        return x

    def Coo(self, y):
        # Coo의 내용
        result = y ** 2  # 예시로 내부매개변수에 5를 더하는 연산을 수행
        print(result)
        return result

# 클래스 인스턴스 생성
my_instance = MyClass()

# Wee 메서드 호출
answer = my_instance.Wee(5)
print(answer)
