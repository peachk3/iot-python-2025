# 파일입출력
# 파일을 오픈, 읽고, 쓰고, 닫음
# 파일 경로 : 파일이 컴퓨터 상에 들어있는 위치 

# 경로 구분자 / \ 다 사용 가능
# mode : r(읽기), w(쓰기), a(추가), ...
# encoding : 한글만(euc-kr, cp949), 국제어(utf-8)

# 상대 경로 - 경로를 특수문자로 생략하는 법
# . : 현재 자기 폴더 위치
# .. : 자신의 부모 폴더 위치
f = open('./day03/test.txt', mode='w', encoding='utf-8') # -> day03 폴더 안에 test 파일 생성 

## 절대 경로 - 드라이브부터 모든 경로를 다 작성
# f = open('C:/Source/iot-python-2025/day03/test2.txt', mode='w', encoding='utf-8')
# f = open('../test3.txt', mode='w', encoding='utf-8') # -> Source 파일 안에 test3 파일 생성

# \를 문자열에 표현하고 싶으면
# f = open('C:\\Source\\iot-python-2025\\day03\\test4.txt', mode='w', encoding='utf-8')

f.write('파일 쓰기 시작!\n') # write 는 print()와 다르게 자동 줄바꿈 되지 않음!!
f.write('두번째 줄 작성합니다.\n')
# f.write('\n')

f.close()

print('파일 쓰기 완료')

r = open('./day03/test.txt', mode='r', encoding='utf-8') 

while True:
    line = r.readline() # 한 줄씩 읽음
    if not line: # 한 줄 읽은 값이 None이면
        break # while문을 탈출하라

    # print(line, end='')
    print(line.replace('\n', ''))

r.close()

