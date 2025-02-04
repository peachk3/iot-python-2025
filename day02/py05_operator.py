# 연산자

# 사칙연산 : + - * /
a, b = 15, 14
# Shift + Del 는 한 줄 삭제
print(a + b)
print(a - b)
print(a * b)

# 나누기 연산자 /, //, %
a = 14
b = 4
print(a / b) # 나눈 결과는 float
print(a // b) # 나눈 몫, int
print(a % b) # 나머지, int

# 거듭제곱(Power)
print(2 ** 10)

# 연산자 우선순위
## 계산식이 복잡해서 연산자 우선순위를 잘 모르겠으면 () 사용
print((3 + 4) * 7)
print(3 + (4 * 7))


## 리스트 연산
## last index = len(list) - 1
listSample = [1, 3, 5, 7, 9]
print(listSample[0])
print(len(listSample)) # 리스트의 길이

print(listSample[1])
print(listSample[2])
print(listSample[3])
print(listSample[4])

listSample[4] = 11

print(listSample[len(listSample) - 1])
# print(listSample[5]) ## 5번째의 값 X 

## 문자열 연산 : +, * 만 존재
greeting = 'Hello'
target = 'World'
print(greeting, target) # 문자열 연산 X, 2개의 변수 하나씩 출력함
print(greeting + ' ' + target) # 문자열 연산 + string concatenate
print('{0} {1}'.format(greeting, target))
print(f'{greeting} {target}')

print(greeting * 5) # 해당 문자열을 * 수로 반복

## 문자열(Charactor Array) : List와 유사하지만 값 수정 불가
print(greeting[1]) # 리스트 연산
# greeting[0] = 'C' # 오류 발생
print(greeting)

## 리스트연산, 슬라이싱
listSample =['2', '0', '2', '5', '-', '0', '2', '-', '0', '4']
current = '2025-02-04'

for i in listSample:
    print(i, end='')
print()

print(current)
# 준비 끝

# 인덱싱, 인덱스에 있는 값을 가져오기
print(listSample[-1]) # 오른쪽에서 시작일 경우 -1에서부터 시작
print(current[-1]) # == print(current[9])

# 슬라이싱, 리스트를 자르기
## [start:end] : end - 1까지만 추출
print(listSample[0:3 + 1]) # => ['2', '0', '2', '5']
print(current[0:4]) # => 2025

# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 + 1]
day = current[8:] # end 끝까지는 숫자 생략
print(year, month, day)
print(current[-2:]) # day
print(current[-5: -3]) # month
print(current[-10:-6]) # year

## 문자열 연산 중 함수를 사용
full_name = "Peach DG. Park"
# 자르기
print(full_name.split())
print(full_name.split(' '))

names = full_name.split(' ')
print(type(names)) # 리스트
print(names)
print(names[0]) # Park

names = full_name.split('.')
print(type(names))
print(names)

# 바꾸기
print(full_name.replace('Peach DG.','Ashely'))

# 공백제거
origin = '     Hello  ~     '
print(f'//{origin}//')
print(f'//{origin.lstrip()}//') # 왼쪽 공백 제거
print(f'//{origin.rstrip()}//') # 오른쪽 공백 제거
print(f'//{origin.strip()}//') # 양쪽 공백 제거

# 단어 찾기
full_name = "Peach DG. Park"
print(full_name.find('D'))
print(full_name.find('e'))
print(full_name.find('d')) # -1 : 찾을 수 없음


print(full_name.count('a')) # 문장에 몇 번 존재
# print(full_name.index('d')) # 오류 발생

print(full_name.upper()) # 모든 글자 대문자 
print(full_name.lower()) # 모든 글자 소문자

## T로 자를때
# '', "" == Empty(비어있다)
# ' ', " " == Space(공백존재)
origin = 'TESTSTRING'
print(origin.split('T')) # -> ['', 'ES', 'S', 'RING'] T를 자르면 앞에 비어있음! Empty

