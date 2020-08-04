# Flask_web
[ VSCODE를 이용한 플라스크 개발환경 설정 ]
0) 가상환경이란?


1) VSCODE 프로그램 설치
https://code.visualstudio.com

2) 작업폴더 생성 및 워크스페이스 등록  
  예) c:/mulcamFlask 
  [File]-[Add Folder To workspace]

3) 파이썬(아나콘다) 설치 
터미널에서 확인 
[Terminal]-[New Terminal]

>> python 
>> exit()

4) 가상환경 설정 : python 
# virtualenv 모듈 확인 
>> pip list 

# virtualenv 없으면 설치
# pip install virtualenv

# 가상환경 생성
virtualenv .venv

# 가상환경 활성화
# Mac OS / Linux
source .venv/bin/activate

# Windows
#.venv\Scripts\activate 

>cd .venv/Scripts
>activate


# (venv) 프롬프트 나오면 성공
(venv) 프롬프트 

# 비활성화 
(venv) deactivate


4-1) 아나콘다 가상환경 설정은?
# 'something`이라는 이름의 가상환경 (python 버전 3.7.3)
conda create --name something python=3.7.3 pip
# 가상환경 활성화
conda activate something

5) 플라스크 관련 모듈 설치 
.venv\Scripts\activate 
(venv) pip install flask
(venv) pip list


6) VScode Extension 설치 
- Python : ms-python


7) 가상환경모드에서 파이썬 파일 실행하기 
#helloPython.py 
print('Hello Python')
print('Hello Flask')

(.venv) cd..
(.venv) cd..
(.venv) python helloPython.py

---------------------------------------

## 플라스크 가상환경 생성하기 - 파이참 
1) [File]-[New Project]
2)  작업폴더 지정 
  c:/workspaceFlask
3) Project Interpretre 에서 가상환경 설정 
  그림참조 
4) [Open New Window] 클릭해서 프로젝트 생성 
5) 파이참의 [Project] 윈도우에서 생성 목록 확인 

// 가상환경 활성화 
1) 파이참 터미널창 실행 
2) cd venv/Scripts
3) activate
4) 프롬프트 확인 
5) deactivate 
가상환경 비활성화 




---------------------------------------------------
[ Hello World app 만들기 ]
---------------------------------------------------
#실습 소스 : step1>app.py

# app.py
# flask 모듈 임포트
from flask import Flask

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
# 함수 등록
def hello():
    return 'Hello World'

# 앱 실행
# 웹주소와 포트 지정
# 127.0.0.1:5000
app.run(host='127.0.0.1', port=5000, debug=True)
# localhost:5000
# app.run(host='0.0.0.0', port=5000, debug=True)



# 결과 확인은?
# 터미널창에서 cd 작업폴더
# python app.py
# 주소가 표시되면 [Ctrl]누른 상태에서 클릭
# 서버종료시에는
# 터미널창에서 [Ctrl]+[C]
# 웹브라우저에서 Hello World 확인 



# app.py  내용 수정후 저장 
# 웹브라우저에서 새로고침에서 확인 



---------------------------------------------------
[ return HTML태그 반환 ]
---------------------------------------------------
# 라우터 등록함수에 HTML 태그를 반환하려면?
# return 'HTML 태그'

# 문제점 
# => 태그 모두 입력해야하는 불편함 
# => render_template로 해결

실습 소스 >> 
step2>app.py

# 수정소스 부분 
@app.route('/')
def hello():
    # HTML 태그를 직접 return 문을 이용하여 반환한다.
    return '<h1>Hello World</h1><h2>flask</h2>'





---------------------------------------------------
[ Jinja2의 render_template() - HTML 문서 연결하기 ]
---------------------------------------------------
# render_template()
# - @app.route 함수 등록시 return 값으로 html 문서를 연결한다.  
# - 연결되는 html 문서는 templates 폴더에 저장되어 있어야 한다. 
# - render_template 모듈 임포트 
# from flask import render_template

# 작업 과정 
# 1) templates 폴더 생성 후 index.html 문서 생성 
# 2) app.py 파일 생성 
# 3) 관련 모듈 임포트 
# from flask import render_template
# 4) 앱생성시 연결되는 index() 함수의 return 값으로 
# render_template(연결html파일) 호출 

#) 예
@app.route('/')
def index():
    return render_template('index.html')



---------------------------------------------------
[ 라우팅(Routing)과 주소 생성 ]
---------------------------------------------------
라우터데코레이터 : 주소와 뷰함수 등록 
@app.route('/주소'):
   def 뷰함수():
        return render_template('연결페이지경로')


1) templates 폴더에 연결할 html 문서 생성 
   index.html 
   second.html
   third.html

  ul>(li>a)*3 으로 서로 페이지 주소 연결 

예)
<ul>
    <li><a href="/">index</a></li>
    <li><a href="/first">first</a></li>
    <li><a href="/second">second</a></li>
    <li><a href="/third">third</a></li>
</ul>


2) app.py에 4개의 라우터 등록 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/second')
def second() :
    return render_template('second.html')

@app.route('/third')
def third() :
    return render_template('third.html')

3) 웹브라우저에서 확인 
http://127.0.0.1:5000/
http://127.0.0.1:5000/first
http://127.0.0.1:5000/second
http://127.0.0.1:5000/third


# 실습 소스 >> 
step4/templates/index.html, second.html, third.html
step4/app.py

# app.py
# flask 모듈 임포트
from flask import Flask
# html 연결 페이지 기능 모듈 임포트
from flask import render_template

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록1 => 웹상 루트 주소 생성
@app.route('/')
# 함수 등록
# 루트주소와 연결된 html 페이지 등록 함수.
# html 파일의 기본 폴더 위치는 templates
def index():
    return render_template('index.html')

# 라우터 등록 2
@app.route('/first')
def first():
    return render_template('first.html')

# 라우터 등록 3
@app.route('/second')
def second():
    return render_template('second.html')

# 라우터 등록 4
@app.route('/third')
def third():
    return render_template('third.html')

# 앱 실행
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)

# 결과 확인은?
# 터미널창에서 python app.py
# 주소가 표시되면 [Ctrl]누른 상태에서 클릭
# 서버종료시에는
# 터미널창에서 [Ctrl]+[C]



---------------------------------------------------
[ Request 요청방식 - GET/POST]
---------------------------------------------------
// Request 요청방식 이해하기 
get : 검색어와 같이 값이 전달. 
post : 데이타 저장과 같이 많은 양의 데이타 전달

// request 모듈 임포트 
from flask import request

// 라우터에 요청방식 등록하기 
app.route("/주소", methods=[요청방식])
def 함수명():
   return render_template(html문서경로)

# 요청 방식 : get, post 등등
methods=['GET']
methods=['POST']
methods=['GET', 'POST']
# post : form 태그의 method='post'인 경우
# get : 주소를 직접 입력했을 때, a 태그를 클릭 했을 때
#       form 태그의 method가 없거나 get인 경우



1) templates 폴더에 index.html 생성 
- 3가지스타일의 FORM 지정 

<h2>method:GET</h2>
<form action="/second" method="get">
        <button type="submit">확인</button>
</form>

<h2>method:POST</h2>
<form action="/second" method="post">
        <button type="submit">확인</button>
</form>

<h2>method None</h2>
<form action="/second">
        <button type="submit">확인</button>
</form>

2) templates 폴더에 result.html 생성 
- form.html 문서에서 폼의 action으로 사용 
- / 로 이동하는 하이퍼링크 태그 생성 

<a href="/">처음으로</a>

3) app.py 파일 생성 

# request 모듈 임포트 
from flask import request

4) GET, POST를 request.method로 터미널창에 출력하도록
라우터와 함수 등록 
 
@app.route('/result', methods=['GET','POST'])
def result():
    # 요청 방식 터미널창에 표시하기
    print('요청방식 : ', request.method)
    return render_template('result.html')




---------------------------------------------------
[ Request 요청방식에 따라 html 분기하기 ]
---------------------------------------------------

1) POST, GET 방식에 따라 분기하는 페이지 생성 
templates/get.html
templates/post.html

2) form.html 생성 
- 3가지스타일의 FORM 지정 

<h2>method:GET</h2>
<form action="/result" method="get">
        <button type="submit">확인</button>
</form>

<h2>method:POST</h2>
<form action="/result" method="post">
        <button type="submit">확인</button>
</form>

<h2>method None</h2>
<form action="/result">
        <button type="submit">확인</button>
</form>


3) app.py 파일 생성 

# request 모듈 임포트 
from flask import request

4) 라우터 등록. 
GET, POST 방식에 따라 
터미널에 출력후 
IF .. ELSE로 분기 

@app.route("/result", methods=['GET', 'POST'])
def result() :
    # 요청 방식 터미널창에 표시하기
    print('요청방식 : ', request.method)
    # GET과 POST 방식에 따라 HTML 분기하기
    if request.method == 'POST':
        return render_template('post.html')
    else:
        return render_template('get.html')





---------------------------------------------------
07. [ 데이터 전달과 데이터 받기 - GET ]
---------------------------------------------------
// GET 과 POST
# get : 파라미터 데이터를 주소에 붙혀서 보낸다. 
#       주소에 직접 붙여서 보내기 때문에 전체 용량이 적다. 이 때문에 속도가 빠르다.
#       영문,숫자,특수문자 일부만 가능하며 전체 주소가 255글자 이상을
#       넘지 못한다는 단점을 가지고 있다.
# post : 파라미터 데이터를 요청 정보 내부에 숨겨서 보낸다.
#        부가 정보가 추가로 들어가기 때문에 전체 용량이 get보다 많으며
#        이 때문에 속도가 느리다.
#        모든 문자를 전달할 수 있으며 길이에 제한이 없다.
# 사용자에게 입력받는 데이터 => post, 그 외 => get

// 하이퍼링크 주소로 변수와 값 전달형식 : ?이용 
URL?변수1=값1&변수2=값2...


// GET 방식의 폼안에 텍스트필드로 값 전달 형식 
<input type="text" name="변수" >


// GET 방식의 전달받은 값 호출
# request.args['변수']
# request.args.get('변수')
# request.values.get('변수')

// 라우터 함수에서 return문으로 전달받은 값을 반환하려면?
# return '문자열 : ' + 변수
# return f'문자열 : {변수}'


// 테스트 과정 
1) templates/formGet.html 파일 생성 

2) GET 방식으로 주소에 데이터 전달하는 하이퍼링크 생성 


<h2>GET 방식으로 URL에 데이터 전달하기</h2>

<a href="/result?data1=111&data2=222">result</a><br/>
<a href="/result?data1=문자열1&data2=문자열2">result</a><br/>

3) GET 방식으로 폼 안의 텍스트필드로 데이터 전달하기
<!-- <input type="text" name="변수" >  -->
<form action="/result">
    <input type="text" name="data1" placeholder="data1"/><br/>
    <input type="text" name="data2" placeholder="data2"/><br/>
    <button>확인</button>
</form>

4) app.py 생성 
- 입력받은 데이터값을 변수에 저장한 후 return 문으로 반환 

# request.args['변수']
# request.args.get('변수')
# request.values.get('변수')

# return 문에 값 반환은?
# return '문자열 : ' + 변수
# return f'문자열 : {변수}'

@app.route("/result", methods=['GET'])
def result() :
    data1 = request.args['data1']
    data2 = request.args.get('data2')
    data3 = request.values.get('data2')
    return  'data1 : ' + data1 +  ' , data2 : ' + data2 +  ' , data3 : ' + data3
    # return f'data1 : {data1}, data2 : {data2}, data3 : {data3}'




---------------------------------------------------
08 [ 데이터 전달과 데이터 받기 - POST ]
---------------------------------------------------

// POST 방식의 폼안에 텍스트필드로 값 전달 형식 
<input type="text" name="변수" >


// POST 방식의 전달받은 값 호출
# request.form['변수']
# request.form.get('변수')
# request.form.values.get('변수')

// 라우터 함수에서 return문으로 전달받은 값을 반환하려면?
# return '문자열 : ' + 변수
# return f'문자열 : {변수}'

1) templates/formPost.html 파일 생성 

2) POST 방식으로 폼 안의 텍스트필드로 데이터 전달하기
<form action="/result" method="post">
    <input type="text" name="data1" placeholder="data1"/><br/>
    <input type="text" name="data2" placeholder="data2"/><br/>
    <button>확인</button>
</form>

4) app.py 생성 
- 입력받은 데이터값을 변수에 저장한 후 return 문으로 반환 

# POST 방식으로 라우터 등록
# 텍스트필드로 전송된 값 호출
# request.form['변수']
# request.form.get('변수')
# request.form.values.get('변수')

# return 문에 값 반환은?
# return '문자열 : ' + 변수
# return f'문자열 : {변수}'

@app.route("/result", methods=['POST'])
def result() :
    # 파라미터 데이터를 추출한다.
    data1 = request.form['data1']
    data2 = request.form.get('data2')
    data3 = request.values.get('data2')
    return f'data1 : {data1}, data2 : {data2}, data3 : {data3}'





---------------------------------------------------
09. 데이터 전달과 데이터 받기 - GET/POST
---------------------------------------------------

// 
// app.py에서 GET 방식과 POST 방식에 따라 조건분기한다.


1) templates/formGetPost.html 파일 생성 
<!-- GET, POST 모두 입력 -->

<h2>GET 방식으로 URL에 데이터 전달하기</h2>
<a href="/result?data1=111&data2=222">result</a><br/>
<a href="/result?data1=문자열1&data2=문자열2">result</a><br/>

<h2>GET 방식으로 폼안의 텍스트필드로 데이터 전달하기</h2>
<form action="/result">
    <input type="text" name="data1" placeholder="data1"/><br/>
    <input type="text" name="data2" placeholder="data2"/><br/>
    <button>확인</button>
</form>


<h2> POST 방식으로 데이터 전달하기</h2>
<form action="/result" method="post">
    <input type="text" name="data1" placeholder="data1"/><br/>
    <input type="text" name="data2" placeholder="data2"/><br/>
    <button>확인</button>
</form>


2) app.py 생성 
- GET 방식인지 POST 방식인지에 따라 분기하여 return 문 호출 
request.method 이용 

# GET 으로 지정
# 주소줄의 변수에 저장된 값 호출
# request.args['변수']
# request.args.get('변수')
# request.values.get('변수')

# POST 방식으로 라우터 등록
# 텍스트필드로 전송된 값 호출
# request.form['변수']
# request.form.get('변수')
# request.form.values.get('변수')

# return 문에 값 반환은?
# return '문자열 : ' + 변수
# return f'문자열 : {변수}'


@app.route('/result', methods=['GET', 'POST'])
def result():
    # data3은 미리 if문 밖에 정의. 로컬변수 
    data3 = request.values.get('data2')
    # 요청 방식으로 분기한다.
    if request.method == 'POST':
        # 파라미터 데이터를 추출한다.
        data1 = request.form['data1']
        data2 = request.form.get('data2')

        return f'data1 : {data1}, data2 : {data2}, data3 : {data3}'

    elif request.method == 'GET':
        # 파라미터 데이터를 추출한다.
        data1 = request.args['data1']
        data2 = request.args.get('data2')
        return f'data1 : {data1}, data2 : {data2}, data3 : {data3}'

    return 'Hello World'






---------------------------------------------------
10. 쿼리스트링 
---------------------------------------------------
쿼리스트링(Query String)이란?
 사용자가 웹프로그램으로 입력 데이터를 전달하는 방식

// 주소URL뒤에 <값>을 리턴하기
 /주소/<값1>/<데이타형:값2>


# 테스트 과정 

1) app.py 생성 

# 주소URL뒤에 <값>을 리턴하기
# /주소/<값1>/<데이타형:값2>
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/user/<username>/<int:age>')
def show_user_profile_age(username, age):
    return 'Username %s, 나이 %d' % (username, age)

2) 웹브라우저에서 결과 확인 
http://127.0.0.1:5000/user/Maria
http://127.0.0.1:5000/user/Maria/23

3) templates/index_queryString.html 파일 생성 
# 접속 주소에 따라 등록 라우터에 따라 값 출력하기 

<a href="test1">test1</a><br/>
<a href="test1/sub1">test1 sub1</a><br/>
<a href="test1/sub2">test1 sub2</a><br/><br/>

<a href="test2/100">test2 100</a><br/>
<a href="test2/200">test2 200</a><br/><br/>

<a href="test2/100/101">test2 100 101</a><br/>
<a href="test2/200/201">test2 200 201</a><br/><br/>


<a href="test3">test3</a><br/>
<a href="test4">test4</a><br/><br/>


<a href="test5">test5</a><br/>
<a href="test5/100">test5 100</a><br/>
<a href="test5/100/200">test5 100 200</a><br/>


4) app.py에 라우터 등록 

# 주소 URL에 따라 return 값 출력하기 1
@app.route('/test1')
def test1() :
    return 'test1 <br> <a href="/">index</a>'

@app.route('/test1/sub1')
def test1_sub1() :
    return 'test1 sub1 <br> <a href="/">index</a>'

@app.route('/test1/sub2')
def test1_sub2() :
    return 'test1 sub2 <br> <a href="/">index</a>'


# 주소 URL에 따라 return 값 출력하기 2
# 주소URL 형식
# @app.route('/url/<데이타변수1>/<데이타변수2>')
# 등록함수에서 데이타변수 출력
# return '문자열 : ' + 변수
# return f'문자열 : {변수}'

@app.route('/test2/<data1>')
def test2_data1(data1) :
    return f'test2 data1 : {data1} <br> <a href="/">index</a>'

@app.route('/test2/<data1>/<data2>')
def test2_data1_data2(data1, data2) :
    return f'test2 data1 : {data1}, data2 : {data2} <br> <a href="/">index</a>'

# 2개의 라우터에 하나의 함수 등록
# @app.route('/주소1')
# @app.route('/주소2')
# def 함수명() :
#   return 값

@app.route('/test3')
@app.route('/test4')
def test3_or_test4() :
    return f'test3 or test4 <br> <a href="/">index</a>'
    


---------------------------------------------------
11. [ 템플릿사용
       - 리스트, 딕셔너리, 튜플 정의 후 웹 페이지로 출력] 
---------------------------------------------------
// app.py에서 딕셔너리, 튜플, 리스트 정의후 html 파일에서 출력하기 

1) 파이썬 파일 app.py 에서 
   라우터 함수안에 
   변수와 집합형 변수(딕셔너리, 튜플, 리스트 ...) 정의 

2) 라우터 함수안의 return 문과 render_template 로 변수 값 전달 
   
   return render_template('html파일명', 변수이름1=변수이름2...)

   예)
    @app.route('/')
    def index():
        # 리스트 생성
        test_list = [100, 200, 300, 400]

        # 변수 생성
        userName = '홍길동'

        return render_template('index.html',test_list=test_list, userName=userName)

3) 연결된 html 문서에서 라우터 함수로 전달된 변수 전달받아 출력하기 
    {{변수명}} 으로 변수값 출력 
    {{딕셔너리.키}} 로 딕셔너리값 출력
    {{리스트이름[인덱스]}} 로 리스트값 출력
    {{튜플이름[인덱스]}} 로 튜플값 출력



---------------------------------------------------
12. [ 템플릿사용 - for..range.. 문 이용하기 ]
---------------------------------------------------

// HTML 문서에서 파이썬 반복문 for 이용하기

{% for i in range(start, end, step) %}
  {{ 변수나 값 }}
{% endfor %}

// 중첩 for 문
{% for i in range(start, end, step) %}
    {% for j in range(start, end, step) %}
        {{ 변수나 값 }}
    {% endfor %}
{% endfor %}






---------------------------------------------------
13. [ 템플릿사용 - for 문을 이용하여 콜렉션 데이타값 출력하기 ]
---------------------------------------------------
// app.py에서 리스트, 튜플, 딕셔너리 정의 후
   html 문서에서 for.. 이용하여 출력하기

# for .. in 문을 이용한 집합형 데이타 출력 

   for i in 리스트이름:
    명령문

   for i in 튜플이름:
    명령문

   for key in 딕셔너리이름:
        print(key, 딕셔너리[key])

   for key, value in 딕셔너리.items():
        print(key,' : ', value)


// 실습 과정 

1) app.py 에서 집합형 자료 정의 후 return 문을 이용하여 전송 

def index() :
    # 리스트 정의
    test_list = ['붉은돼지', '라이온킹', '토토로']
    for i in test_list:
        print(i)

    # 튜플 정의
    test_tuple = (10, 20, 30, 40, 50)
    for i in test_tuple:
        print(i)

    # 딕셔너리 정의
    test_dic = {
        'key1' : 100,
        'key2' : 'abcdefg'
    }
    for key in test_dic:
        print(key, test_dic[key])

    for key, value in test_dic.items():
        print(key,' : ', value)

    return render_template('index_forIn.html', test_list=test_list,
                    test_tuple=test_tuple, test_dic=test_dic )


2) HTML 문서에서 {% for i in ... %} ~ {% endfor %} 로 데이타 출력 

    <h2> 리스트 </h2>

    <ul>
    {% for i in test_list %}
        <li>{{i}}</li>
    {% endfor %}
    </ul>
    <h2> 튜플 </h2>

    <ul>
    {% for i in test_tuple %}
        <li>{{i}}</li>
    {% endfor %}
    </ul>


    <h2> 딕셔너리 </h2>

    <ul>
    {% for key in test_dic %}
        <li>{{test_dic[key]}}</li>
    {% endfor %}
    </ul>
    <hr>
    <ul>
    {% for key, value in test_dic.items() %}
        <li>key : {{ key }}, value : {{ value }} </li>
    {% endfor %}
    </ul>






---------------------------------------------------
14. 템플릿사용 - if 문을 이용하기
---------------------------------------------------
// html 문서에서 제어문 이용하기

    {% if 조건식 %}
        {{ 값 }} 또는 태그, 문자열
    {% elif 조건식 %}
        {{ 값 }} 또는 태그, 문자열
    {% else %}
        {{ 값 }} 또는 태그, 문자열
    {% endif %}


// 실습 과정 

1) app.py 에서 변수와 값 지정
@app.route("/")
def index() :
    age = 12
    n = 12
    return render_template('index.html', userAge = age, n = n )

2) index.html 에서
  데이타값에 따라 메세지 출력하기
    <h2> userAge 에 따라 메세지 출력하기  </h2>

    {% if userAge >= 20 %}
        <p> {{userAge}} : 성인 </p>
    {% else %}
        <p> {{userAge}} : 미성년자 </p>
    {% endif %}

    <h2> 양수,음수,0 메세지 출력하기  </h2>
    {% if n > 0 %}
        <p> {{n}} : 양수 </p>
    {% elif n == 0 %}
        <p> {{n}} : 0 </p>
    {% else %}
        <p> {{n}} : 음수 </p>
    {% endif %}




---------------------------------------------------
15. [템플릿사용 - 폼에서 입력받아 연산 결과 출력하기]
---------------------------------------------------

// HTML 폼에서 입력받은 데이터를 파이썬 파일에 전달한 후 웹문서에 출력하기 


1) index.html 파일에 폼 생성

<!-- method 값을 post 로 지정. action 값은 처리 라우터 등록 주소 -->
<!-- name은 전달 변수로 지정 -->
<h2> POST 방식으로 데이터 전달하기</h2>
<form action="/cal" method="post">
    <input type="text" name="data1" placeholder="data1"/><br/>
    <input type="text" name="data2" placeholder="data2"/><br/>
    <button>확인</button>
</form>

2) app.py에서 데이타 파라미터 추출후 변수 저장
   cal.html에 데이터 전달

# request.form['변수']로 변수값 전달 
@app.route("/cal", methods=['POST'])
def result() :
    # 파라미터 데이터를 추출한다.
    data1 = request.form['data1']
    data2 = request.form['data2']
    # 아래는 String이라서 오류 발생 => 자료형 변환 필요
    # return render_template('cal.html',data1=data1, data2=data2)
    return render_template('cal.html',data1=int(data1), data2=int(data2))

3) templates/cal.html 파일 생성 후
   전달받은 데이터를 이용하여 계산식 완료
   {{변수}} 로 연산식 적용해서 출력 


    <ul>
        <li>{{data1}} + {{data2}} = {{data1+data2}} </li>
        <li>{{data1}} - {{data2}} = {{data1-data2}} </li>
        <li>{{data1}} * {{data2}} = {{data1*data2}} </li>
        <li>{{data1}} / {{data2}} = {{data1/data2}} </li>
    </ul>





-------------------------------------------------------------------------------
16. [템플릿사용 - GET 방식으로 데이타 전달받아 결과 출력하기]
-------------------------------------------------------------------------------


// HTML 폼에서 GET 방식으로 입력받은 데이터를 파이썬 파일에 전달한 후 웹문서에 출력하기 

request.args['변수']


1) index.html 파일에 폼 생성

<!-- method 값을 get 로 지정. action 값은 처리 라우터 등록 주소 -->
<!-- name은 전달 변수로 지정 -->
 <h2> 2개의 값을 입력받아라 </h2>
  <form action="/resultCal" method="get">
    <input type="text" name="data1" placeholder="첫번째 숫자 입력"> <br>
    <input type="text" name="data2" placeholder="두번째 숫자 입력">
    <button>확인</button>
  </form>


  <h2> 숫자값을 입력받은 후 구구단 출력하기 </h2>
  <form action="/resultGugu" method="get">
    <input type="text" name="myNumber" placeholder="숫자 입력">
    <button>확인</button>
  </form>


  <h2> 누적합 출력하기 </h2>
  <form action="/resultSum" method="get">
    <input type="text" name="myNumber2" placeholder="숫자 입력">
    <button>확인</button>
  </form>


2) app.py에서 데이타 파라미터 추출후 변수 저장
   html 출력 파일에 데이터 전달

# request.args['변수']로 변수값 전달 
# GET 방식으로 값을 전달받아서 특정 변수에 저장하기
# 데이타변수1 =  request.args['텍스트필드변수명']
@app.route('/resultCal', methods=['GET'])
def result():
    data1 = request.args['data1']
    data2 = request.args['data2']
    print(data1, data2, request.method)
    return render_template('resultCal.html', data1=int(data1), data2=int(data2))


@app.route('/resultGugu', methods=['GET'])
def resultGugu():
    myNumber = request.args['myNumber']
    print(myNumber)
    return render_template('resultGugu.html', myNumber=int(myNumber))

@app.route('/resultSum', methods=['GET'])
def resultSum():
    myNumber2 = int(request.args['myNumber2'])
    print(myNumber2)
    resultSum = 0
    for i in range(1, myNumber2+1) :
        resultSum += i

    return render_template('resultSum.html', myNumber2=int(myNumber2), resultSum=resultSum )


3) templates/파일명.html 파일 생성 후
   전달받은 데이터를 이용하여 계산식 완료
   {{변수}} 로 연산식 적용해서 출력 


    <ul>
        <li>{{data1}} + {{data2}} = {{data1+data2}} </li>
        <li>{{data1}} - {{data2}} = {{data1-data2}} </li>
        <li>{{data1}} * {{data2}} = {{data1*data2}} </li>
        <li>{{data1}} / {{data2}} = {{data1/data2}} </li>
    </ul>









-------------------------------------------------------------------------------
17. [템플릿사용 - GET 방식으로 하이퍼링크로 데이타 전달하고 결과 출력하기]
-------------------------------------------------------------------------------

// GET 방식으로 하이퍼링크로 데이타 전달하고 결과 출력하기

- 하이퍼링크로 변수와 값 전달 
<a href="/라우터주소?변수1=값1&변수2=값2">...</a>

- get 방식으로 변수와 갑 전달받아 처리하기 
변수1 = request.args['변수1']

- html 결과 값 출력하기 
{{ 변수 }}



1) index.html 파일

<h2>GET 방식으로 URL에 데이터 전달하기</h2>
<!--
/라우터에등록한URL?변수1=값1&변수2=값2...
-->
<a href="/cal?num=3">3단 출력</a><br/>
<a href="/cal?num=11">11단 출력</a><br/>
<hr/>



2) app.py
# GET 방식으로 값을 전달받아서 특정 변수에 저장하기
# 데이타변수 = request.args['데이타변수']
@app.route('/resultAge', methods=['GET'])
def result():
    userAge = request.args['userAge']
    print(userAge, type(userAge))
    return render_template('resultAge.html', userAge=userAge)

...


3) resultAge.html
<h2> userAge => {{ userAge }}</h2>






---------------------------------------------------------------
18. 템플릿사용 - 쿼리스트링 방식으로 데이터값 입력받아 결과 출력하기 
---------------------------------------------------------------
// 쿼리스트링 방식으로 데이터값 입력받아 결과 출력하기 

- html 문서에서 하이퍼링크 태그로 값 전달하기 
<a href="/라우터주소/값1/값2..."> ... </a>

- app.py 파일에서 라우터함수안에 '라우터주소/<자료형:변수>'로 데이타값 전달받기 
- 변수로 저장후 render_template()로 데이타값 전달하기 


@app.route('/라우터주소/<자료형:변수>')
def 라우터함수(변수) :
    변수 = 변수
    ...
    return render_template('html문서명', 변수=변수)

- html 문서에 출력하기 
{{ 변수 }}


1) index_get3.html


<h2> 데이터 전달 - 쿼리스트링 </h2>
<ul>
    <li><a href="/resultTotal/50"> num=50, 1~50까지 합구하기 </a></li>
    <li><a href="/resultTotal/100"> num=100, 1~100까지 합구하기 </a></li>
    <li><a href="/resultMul/10/20/30">세수의 곱구하기</a></li>
    <li><a href="/resultInfo/홍길동/1학년/5">학생정보 출력하기</a></li>
</ul>



2) app.py

# 주소URL뒤에 <값>을 리턴하기
# /주소/<값1>/<데이타형:값2>

@app.route('/resultInfo/<userName>/<grade>/<int:no>')
def resultInfo(userName, grade, no):
    userName = userName
    grade = grade
    no = no
    return render_template('resultInfo.html', userName=userName, grade=grade, no=no)




3) resultInfo.html

<h1>학생 정보 출력하기</h1>
<hr>
<ul>
  <li> 학생 이름 : {{userName}}</li>
  <li> 학년 : {{grade}}</li>
  <li> 학번 : {{no}}</li>
  <li> <a href="/">첫 페이지로 이동</a></li>
</ul>





---------------------------------------------------
19. 템플릿 상속과 static 폴더
---------------------------------------------------

// 템플릿 상속이란?
- 웹페이지 문서에서 공통적인 HTML 소스를 삽입하는 기능 
- php, asp 웹프로그래밍 언어의 인클루드 


// 레이아웃이 되는 html 파일에서 변경될 부분만 다음과 같이 설정
{% block 블록이름 %}
실제내용 부분들
{% endblock %}


// 레이아웃을 상속받을 html 파일에서 상속받기 소스
{% extends 'layout.html' %}

// static 폴더 
- html 문서에 삽입되는 이미지, css, js 파일은 별도의 static 폴더에 저장 
- 삽입시 경로는 static/파일이름.확장자 



// 실습 과정 

1) layout.html 
- 레이아웃 파일에 반복되는 공통 메뉴와 카피라이트 지정 
- 내용이 교체되는 블록 구역 정의

<div class="container">
   <!--  공통 메뉴    -->
    <div class="nav">
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/bbs">BBS</a></li>
            <li><a href="/news">News</a></li>
        </ul>
    </div>
    <!--   실제 내용 -->
    <div>
    {% block pageTitle %}{% endblock %}
     <hr>
    {% block contents %}{% endblock %}
    </div>

    <div>
        <p>copyrights&copy;FlaskWorld</p>
    </div>
</div>


2) layout.html 파일을 상속받아 서브 파일 생성
  home.html , about.html, bbs.html, news.html
  - staic 폴더에 삽입 이미지 복사 붙여넣기 
  - layout.html 파일 상속받기 
  - 교체 내용은 block 정의 부분안에 삽입 


<!--layout.html 공통부분 상속 -->
{% extends 'layout.html' %}

{% block pageTitle %}
<h1> Home </h1>
{% endblock %}

{% block contents %}
<p>시작페이지</p>
<div>
    <img src="static/images/course01.jpg" alt="course01">
</div>
{% endblock %}


3) app.py 에서 라우팅 => 주소 생성

@app.route('/')
def home():
    return render_template('home.html')

...




