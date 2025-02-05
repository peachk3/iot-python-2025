# for 문 : 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할 값 :
#   구문 안으로

# 아래와 같이 출력되는 프로그램을 작성하시오
'''
최대별 수 : 4
*
**
***
****
'''

# range() 범위를 생성 클래스
# 마지막 수 : max - 1
# range(9) -> range(0, 8)
# range(init, max, add) 
print(range(0, 8, 2))

# for i in [0, 1, 2, 3, 4, 5, 6, 7] : # 이 조건이 참인 동안 반복
# for i in range(0, 8, 2): # ==  for i in [0, 1, 2, 3, 4, 5, 6, 7] :
    # print(i)

# num = int(input('최대 별 수 :'))

# for i in range(1, num + 1) :
#     print('*' * i)'

# 구구단
# 2단부터 2X9 ~ 9X9
# 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6
# 9 x 1 = 9, ... 9 x 9 = 81
# 요구사항 1 - 한 줄에 각 단씩 나오도록
# 요구사항 2 - x*y값이 항상 두 줄씩 표현되도록
# 요구사항 3 - 단 시작을 표시
for x in range(2, 9 + 1) :
    if x == 5: break # x단 반복문에서 나옴 (x단 이전까지 출력)
    # if x == 5 : continue # x단 제외하고 다 나옴

    print()
    print(f'{x}단 시작-!')
    
    for y in range(1, 9 + 1):
        
        # if y == 8 : break
        print(f'{x} x {y} = {x * y:2d}', end='   ')

    print() # 그냥 한 줄 내리기   

print('\n구구단 종료 \n\n')

## 반복문을 빠져나올 때 : break
## 반복문에서 특정 조건을 지나칠 때 : continue
