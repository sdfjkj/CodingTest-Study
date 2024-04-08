class Singer:

    #초기화 메서드는 모양을 마음대로 만들 수 있습니다.
    #인스턴스가 생성될 때 호출됩니다.
    def __init__(self,name = "noname"):
        self.name = name

    #소멸자는 모양이 고정입니다.
    #이 안에서 하는 작업은 외부 데이터와의 연결을 해제하는 것이 일반적입니다.
    #인스턴스가 소멸될 때 호출됩니다.  
    def setName(self,name:str) -> None :
        self.name = name

    def __str__(self) -> str:
        print("나의 이름은", self.name)
        return self.name

    def getName(self) -> str :
        return self.name

    def __del__(self) :
        print("소멸자")  

    #인스턴스 생성
    singer1 = Singer()
    #name 설정
    singer1.setName(name = "가수")
    # print(singer1.getName())
    print(singer1)  


    # singer2 = Singer()
    # print(singer2.getName())
    # #소멸자 > 인스턴스가 다 종료된 후 소멸


    # singer1 = None
    