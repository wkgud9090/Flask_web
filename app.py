from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User : %s' % username

@app.route('/user/<username>/<int:age>')
def show_user_profile_age(username, age):
    return 'Username : %s, 나이 : %d살' % (username, age)

@app.route('/user/<username>/<int:age>/<job>')
def show_user_profile_age_job(username, age, job):
    return 'Username : %s, 나이 : %d살, 직업 : %s' % (username, age,job)

@app.route('/')
def index():
    #return '<h1>Hello World and jahyong</h1><hr><h2>Flask App Start</h2>'
    #return render_template('formPost.html')
    return render_template('index_calForm.html')

@app.route('/cal', methods = ['post'])
def cal():
    data1 = request.form['data1']
    data2 = request.form['data2']
    #return data1 + '<br>' +data2
    return render_template('cal_result.html',data1 = int(data1), data2 = int(data2))
    #myList = ['사과','바나나','딸기']
    #myDict = {100:'백', 200:'이백',300:'삼백'}

@app.route('/gugu', methods = ['post'])
def gugu():
    data3 = request.form['data3']
    return render_template('gugu_result.html',data3 = int(data3))

@app.route('/info', methods = ['get'])
def info():
    userName = request.args['userName']
    userAge = int(request.args['userAge'])
    userYear = 2020 - userAge + 1
    return render_template('info_result.html',userName = userName, userAge = userAge, userYear = userYear)

@app.route('/total', methods = ['post'])
def total():
    data4 = int(request.form['data4'])
    total = 0
    for i in range (1, data4+1):
        total +=i
    return render_template('total_result.html',data4=data4, total = total)

@app.route('/resultTotal/<int:no>')
def resultTotal(no):
    result = 0
    for i in range(1, no+1):
        result +=i
    return render_template('resultTotal.html', no = no, result = result)

@app.route('/test1')
def test1() :
    return '<h1>test1</h1> <br> <a href="/">Start Page</a>'

@app.route('/test1/sub1')
@app.route('/test1/sub2')
def test1_sub1() :
    return '<h1>test1 sub1 또는 test1 sub2</h1> <br> <a href="/">Start Page</a>'

@app.route('/test2/<data1>')
def test2_data1(data1) :
    return f'test2 data1 : {data1} <br> <a href="/">Start Page</a>'

@app.route('/test2/<data1>/<data2>')
def test2_data1_data2(data1, data2) :
    return f'test2 data1 : {data1}, data2 : {data2} <br> <a href="/">Start Page</a>'




@app.route('/second')

def second():
    #return '<h1>second page</h1>'
    return render_template('second.html')

@app.route('/third')
def third():
    #return '<h1>third page</h1>'
    return render_template('third.html')


@app.route('/result', methods=['post'])
def result():
    print('요청방식: ', request.method)
    #return request.method + '<hr><a href="/">첫번째 페이지</a>'


    # GET과 POST 방식에 따라 HTML 분기하기
#    if request.method == 'POST':
#        return render_template('post.html')
#    else:
#        return render_template('get.html')
# localhost:0.0.0.0 5000
#    data1 = request.args['data1']
#    data2 = request.args.get('data2')
#    data3 = request.values.get('data2')
#    return  'data1 : ' + data1 +  ' , data2 : ' + data2 +  ' , data3 : ' + data3 + '<hr><a href = "/"> 첫번째 페이지</a>'
    data1 = request.form['data1']
    data2 = request.form.get('data2')
    data3 = request.form['data1']
    return  'data1 : ' + data1 +  ' , data2 : ' + data2 +  ' , data3 : ' + data3 + '<hr><a href = "/"> 첫번째 페이지</a>'

#app.run(host='localhost', port=5000, debug=True)
app.run(host='127.0.0.1', port =5000, debug=True)