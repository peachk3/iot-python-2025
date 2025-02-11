# GUI를 위한 모듈 
from tkinter import * # tkinter 모듈에 있는 모든 클래스, 함수, 변수 등을 다 쓰겠다
from tkinter.messagebox import *  # 모듈 및에 있는 모듈을 from tkinter import * 로 가져올 수 없음
from tkinter.scrolledtext import * 
from tkinter.font import *

# 제미나이를 위한 모듈
import google.generativeai as genai

# 6. 제미나이 API용 구성
genai.configure(api_key='AIzaSyApt71OA3i1Z4dew4zU-lRcRvuMQcWVfRg') # 신청한 API 키 
model = genai.GenerativeModel('gemini-1.5-flash') # AI 사전훈련된 모델

# 4. 전송버튼 이벤트, 제미나이 실행 포함
def responseMessage():
    # showinfo('실행', 'API를 실행합니다.') #('창 title','알림 내용')
    inputText = textMessage.get('1.0', END).replace('\n','').strip()
    print(inputText)
    textMessage.delete('1.0', END) # 입력창 글 지우기
    # showinfo('결과', inputText) # 다이얼로그, 모달(Modal)창

    if inputText:
        try:
            # user의 질문 화면에 띄우기
            textResult.insert(END, '유저 : ', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user') # 'user' 텍스트 아규먼트

            ai_response = model.generate_content(inputText) # ai에 질문 입력
            response = ai_response.text # 답변 담기

            # ai의 답변 화면에 띄우기
            textResult.insert(END, '챗봇 : ', BOLD)
            textResult.insert(END,f'{response}\n\n', 'ai') # 'ai' 텍스트 태그 아규먼트

        except Exception as e:
            textResult.insert(END, f'Error : {str(e)}\n\n','error')

        finally:
            textResult.see(END) # 스크롤 텍스트 마지막 위치로 스크롤 다운

# 9. textMessage 위젯에서 Enter입력시 전송 버튼 클릭
def keypress(event):
    # print(repr(event.char)) # repr을 사용하지 않으면 \r, \x08... 표시 안 됨
    # \r(캐리지 리턴)  \n(뉴라인) 혼용해서 사용 \r=n, \n, \r
    if event.char == '\r':
        responseMessage()

# 12-1. 종료시 이벤트처리 함수
def onClosing():
    if askokcancel('종료확인','종료하시겠습니까?'): # askyesno() 사용 가능
        root.destroy() # 완전종료

# 1. 메인윈도우 생성
root = Tk()
root.title('Gemini Chatbot')
root.geometry('730x450')

# 13. 아이콘 변경
# ./image/ 경로는 삭제
root.iconbitmap('chatbot.ico') # pyinstaller로 실행파일 폴더에 복사

# 7. 전체에서 사용할 폰트 지정 -> 나눔 고딕
myFont = Font(family='NanumGothic', size=10)
boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

# 2. UI 화면 구성
inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF')
inputFrame.pack(side=BOTTOM, fill=BOTH) # =='bottom'

# 3. inputFrame에 들어갈 Entry와 Button 구성
textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont) # 글자 단위로 wrap(줄바꿈)
# 8. 입력창에서 Enter 입력시 keypress 이벤트 처리 함수 발생
textMessage.bind('<Key>', keypress)
textMessage.pack(side=LEFT, padx=15)

buttonSend = Button(inputFrame, text='전송', bg='green', fg='white', font=myFont, command=responseMessage)
buttonSend.pack(side=RIGHT, padx=20, pady= 3)

# 5. API호출 결과 메시지 출력될 스크롤 기능 텍스트 위젯
textResult = ScrolledText(root, wrap=WORD, bg='#000000', fg='white', font=myFont) # bg='#000000' == black
textResult.pack(fill=BOTH, expand=True)

# 11. 스크롤텍스트에 나올 메시지 디자인
textResult.tag_configure('user', font=boldFont, foreground='yellow')
textResult.tag_configure('ai', font=boldFont, foreground='limegreen')
textResult.tag_configure('error', font=boldFont, foreground='red')

# 10. 실행 후 바로 입력창에 포커스가 가도록
textMessage.focus_set()

# 12. 종료버튼(x)를 누르면 종료메시지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing) 

# 1. 종료시까지 계속 실행
root.mainloop()

