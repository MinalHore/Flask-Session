from flask import Flask,request,jsonify,render_template

app=Flask(__name__)

@app.route('/')
def testfunc():
    return 'This is my Flask App'

@app.route('/<name>/<int:age>')
def testname(name,age):
    return f'Hello my name is,{name} and my age is {age}'    

@app.route('/handle',methods=['GET'])
def test_args_kwargs():

    args=request.args.getlist('args')
    kwargs={key:value for key,value in request.args.items() if key !='args'}

    args_list=list(args)
    kwargs_dict= dict(kwargs)

    result={
        'args':args_list,
        'Kwargs':kwargs_dict
    }
    return jsonify(result)

@app.route('/index')
def index():
    app_name='Ecommerce App'
    list1=['Tushar',29,56.7,0x00123,{'city':'Pune'}]
    
    dict1={
        1001:{'Name':'Tushar','Position':'trainee','salary':20000},
        1002:{'Name':'Pratiksha','Position':'HR','salary':28000},
        1003:{'Name':'Utkarsha','Position':'Tester','salary':32000},
        1004:{'Name':'Sauru','Position':'Developer','salary':35000},
        
    }

    return render_template('index.html',data=app_name,list_data=list1,data_dict=dict1)
    
app.run(debug=True)