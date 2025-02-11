# Tkinter를 클래스화 
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyApt71OA3i1Z4dew4zU-lRcRvuMQcWVfRg') 
model = genai.GenerativeModel('gemini-1.5-flash')

class window(Tk): # 상속
    def __init__(self):
        super().__init__() # 부모 객체도 같이 초기화

        # 메인윈도우 (title, 사이즈 지정)
        self.title('제미나이 챗봇 v2.0')
        self.geometry('730x450')

        # 아이콘 변경
        self.iconbitmap('./image/chatbot.ico')

        # 클래스 작업할 땐 self... 유심히!
        # 종료버튼 클릭시 종료 메시지 확인 후 종료
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        # 윈도우 화면 초기화 멤버함수(메서드)
        self.initWindow()

    def keypress(self, event): # self - window(Tk)참조 /event 매개변수 전달
        if event.char == '\r':
            self.responseMessage()

    # 윈도우 화면
    def initWindow(self):
        # 폰트 지정
        self.myFont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)
        
        # UI 화면 구성
        # input에 프레임 생성
        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
        self.inputFrame.pack(side=BOTTOM, fill=BOTH) # =='bottom'

        # inputFrame 들어갈 Entry, Button 구성
        self.textMessage = Text(self.inputFrame, width=75, height=1, wrap=WORD, font=self.myFont) # 글자 단위로 wrap(줄바꿈)
        
        # 입력창에서 Enter 입력시 keypress 이벤트 처리
        self.textMessage.bind('<Key>', self.keypress)
        self.textMessage.pack(side=LEFT, padx=15)

        # 전송 버튼
        self.buttonSend = Button(self.inputFrame, text='전송', bg='green', fg='white', font=self.myFont, command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT, padx=20, pady= 3)

        # 나머지 부분 복사
        # API 호출 결과 메시지 출력될 스크롤 기능 텍스트 위젯
        self.textResult = ScrolledText(self, wrap=WORD, bg='#000000', fg='white', font=self.myFont) # bg='#000000' == black
        self.textResult.pack(fill=BOTH, expand=True)

        # 스크롤텍스트에 나올 메시지 디자인
        self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow')
        self.textResult.tag_configure('ai', font=self.boldFont, foreground='limegreen')
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')
        
        # 실행 후 바로 입력창에 포커스가 가도록
        self.textMessage.focus_set()

    def responseMessage(self): # 내용 수정
        self.inputText = self.textMessage.get('1.0', END).replace('\n','').strip()
        print(self.inputText)
        self.textMessage.delete('1.0', END)
        # showinfo('동작', f'이제 API를 호출하면 됩니다!\n{self.textMessage.get("1.0", END)}')

        if self.inputText:
            try:
                # user의 질문 화면에 띄우기
                self.textResult.insert(END, '유저 : ', BOLD)
                self.textResult.insert(END, f'{self.inputText}\n\n', 'user') # 'user' 텍스트 아규먼트

                ai_response = model.generate_content(self.inputText) # ai에 질문 입력
                response = ai_response.text # 답변 담기

                # ai의 답변 화면에 띄우기
                self.textResult.insert(END, '챗봇 : ', BOLD)
                self.textResult.insert(END,f'{response}\n\n', 'ai') # 'ai' 텍스트 태그 아규먼트

            except Exception as e:
                self.textResult.insert(END, f'Error : {str(e)}\n\n','error')

            finally:
                self.textResult.see(END) # 스크롤 텍스트 마지막 위치로 스크롤 다운

    def onClosing(self):
        if askokcancel('종료확인','종료하시겠습니까?'): 
            self.destroy() # 완전종료

if __name__ == '__main__':
    print('Tkinter 클래스 시작!')
    app = window() # Tkinter 클래스 객체 생성
    app.mainloop()
