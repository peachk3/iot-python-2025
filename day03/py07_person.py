class Person:
    #명사(속성)인 멤버변수
    name = '루피'
    age = 12
    weight = 10.4
    gender = 'female'

    # 초기화(생성자) 메서드(파이썬 기본으로 포함)
    def __init__(self, name, age, weight, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender

    def __str__(self): # 객체 출력을 문자열 포맷팅
        retStr = f'{self.name}\n{self.age}\n{self.weight}\n{self.gender}'
        return retStr

    # 동사(기상)인 멤버함수(메서드)
    def getup(self): # myself(person 자신)
        print(f'{self.name}이(가) 일어납니다.')

    def setWeight(self, weight):
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 {self.weight}kg')
        self.weight = weight
        print(f'변경 후 {self.weight}kg')
    
    def getGender(self):
        return self.gender

man = Person('재롱', 8, 5.4, 'male') # __init__() 특수함수를 실행 / __함수(스페셜메서드) 
man.getup()
man.setWeight(10.2)
print(f'{man.name}의 성별은 {man.getGender()}.')
print('-----------------------------------------')
print('객체 정보')
print(man)