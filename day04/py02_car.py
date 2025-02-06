# 객체지향 다시

class Car :
    ## __new__(사용빈도 낮), __init__ (사용빈도 높)
    ## Car() 호출하면 아래의 메서드가 실행
    ## company, name, plateNumber 모를때는 None(뭔지 모름)
    def __init__(self, company=None, name=None, plateNumber=None): # self - 자기 자신
        self.__company = company # 멤버변수 이름 앞에 __ 쓰면 외부접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성')

    # 클래스 자체가 출력되는데, __str__문자열로 출력되도록 바꿔줌
    def __str__(self):
        return f'제 차는 {self.__name}이고, 차 번호는 {self.__plateNumber}입니다.'
    
    # 외부에서 잘못된 차번호를 넣으면 안 들어감
    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str :
            self.__plateNumber = newPlateNumber
    
    def setName(self, newName='글쎄요'): # 이름을 모를때 글쎄요로 대체
        self.__name = newName

    def getName(self): # 값가져올 때 get 사용
        return self.__name

# 모듈화하려면 예제 소스는 없어야함 -> 모듈 후 실행 시 전부 실행됨
# myCar = Car('현대','아이오닉','43라0987')
# 파라미터명=값으로 매개변수 순서를 변경 가능
# myCar = Car(name='아이오닉', plateNumber='45라0987', company='현대')

# print(myCar) # 차의 번호를 출력하고 싶음

# myCar.__plateNumber = 2018 # 클래스 외부에서 잘못된 데이터를 넣어도 문제가 발생 X
# print(myCar)

# myCar.setPlateNumber('45라1144')
# print(myCar)

# yourCar = Car()
# print(yourCar)

# yourCar.setPlateNumber('123마0987')
# print(yourCar)

# yourCar.setName() # -> 제 차는 글쎄요이고 (setName에서 newName='글쎄요'로 지정)
# print(yourCar)

# yourCar.setName('제네시스') # -> 제 차는 제네시스이고
# print(yourCar)
