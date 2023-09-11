import flask, os
from flask import *
from flask import render_template as rt 
from flask import Flask 

def get_format(filename):
    splt=filename.split()
    aformt=splt[len(filename)-1]
    return aformt



app=Flask(__name__)
global files
@app.route('/')
def index():
    global files
    files=os.listdir('templates')
    nums=len(files)
    ln=[i for i in range(nums)]

    


    return rt('index.html',files=files,ln=ln)

global files

@app.route('/login',methods=['GET','POST'])
def login():
    id=request.form['aid']
    passwd=request.form['aip']

    if id=='admin' and passwd=='01234':
        pass

    return rt('login.html')

@app.route('/view',methods=['POST','GET'])
def view():
    file_id=request.form['bid']
    findex=int(file_id)
    tf=files[findex]
    
    fdata=open(f'templates/{tf}','r').read()


    return rt('view.html',content=fdata)


#app.run(debug=True)
app.run(host='0.0.0.0')