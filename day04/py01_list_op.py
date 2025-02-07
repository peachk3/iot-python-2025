# 리스트 연산
# 리스트가 for, while 반복문에서 가장 많이 활용되는 자료 구조
# iterable -> 반복할 수 있는 요소가 for, while문에 사용 (반복가능한 것만 for, while문에서 사용 가능!!)
listSample = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10] # 반복

sum = 0
for i in listSample :
    sum = sum + i # sum += i
print(f'합산결과 = {sum}')

# 리스트 연산
arr = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
print(arr)
print(arr[4])
print(arr[0] + arr[2])
print(arr[-2])
print(arr[2:3])

print(arr + arr2)
print(arr * 2) # [1, 2, 3, 4, 5] 두 번 반복

## 리스트 길이
print(len(arr))

arr[2] = 9 # 데잉터 할당
print(arr)

## 리스트 요소 삭제
arr[2] = None
print(len(arr), arr) # None으로 변경

del(arr[2])
print(len(arr), arr) # 자리 삭제

## 리스트 요소 추가
arr.append(7) # 제일 뒤에 추가 / 리스트 안에 리스트 추가
print(arr)

arr.insert(2, 100) # n번째 자리에 숫자 입력
print(arr)

arr.insert(6,100)
print(arr)

# insert, replace 차이점
# insert -> 배열(list)에서 사용 가능
# replace -> 문자열에서 사용 가능

## 리스트 합칠때
print(arr.extend(arr2)) # 두 개의 리스트를 하나의 리스트로 합침

## 리스트 정렬(쇼핑몰 낮은가격순, 높은가격순, 최신일자부터...)
arr = [6, 7, 1, 3, 9, 0, 2, 8]
print(arr)
arr.sort() # 오름차순 정렬
print(arr) 
arr.sort(reverse=True)
print(arr)

## 요소의 위치 파악
print(arr.index(9)) # n이 몇 번째에 있는지 알려줌 / 없는 데이터를 인덱스하면 오류 발생

## 요소꺼내기
print(arr.pop()) # 가장 마지막 인덱스에 있는 값 꺼냄 [9, 8, 7, 6, 3, 2, 1, 0] -> 0
print(arr) # 가장 마지막 인덱스의 값을 제외하고 결과 출력 [9, 8, 7, 6, 3, 2, 1]

## 리스트컴프리핸션 - 대량의 리스트를 쉽게 생성하는 방법
arr = [i for i in range(1, 100 + 1)]
# 좌측 i : 배열에 넣음
# 우측 i : range()에서 생성된 값을 받는 반복 변수
print(arr)

sum = 0
for i in arr:
    sum += i

print(f'{len(arr)}까지의 합산은, {sum}입니다.')

## 추가 설명
# append() 
x = ['W', 'Y', 'Z']
y = ['A', 'C', 'E']

x.append(y)
print(x)
print(len(x)) # => 4
# => ['W', 'Y', 'Z', ['A', 'C', 'E']]

# extend()
x = ['W', 'Y', 'Z']
y = ['A', 'C', 'E']

x.extend(y)
print(x)
print(len(x)) # => 6
# => ['W', 'Y', 'Z', 'A', 'C', 'E']