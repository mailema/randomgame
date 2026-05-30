from flask import Flask,render_template,redirect,session,request
import random
import os

mylist=[]
app=Flask(__name__)
app.secret_key='secret'

@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method=='POST':
        mylist.clear()
        session['f']=request.form['first']
        x=session.get('f')
        a="num" + x
        mylist.append(a)
        session['s']=request.form['second']
        y=session.get('s')
        b="num" + y
        mylist.append(b)
        session['t']=request.form['third']
        z=session.get('t')
        c="num" + z
        mylist.append(c)
        return redirect('/result')
    return render_template('mygame.html')
    
@app.route('/result')
def resultpage():
    score = 0
    random1=random.randint(0,100)
    random2=random.randint(0,100)
    random3=random.randint(0,100)
    random4=random.randint(0,100)
    random5=random.randint(0,100)
    random6=random.randint(0,100)
    mark1=session.get('f')
    mark2=session.get('s')
    mark3=session.get('t')
    if mark1 == "1":
        score += random1
    elif mark1 =="2":
        score += random2
    elif mark1 =="3":
        score += random3
    elif mark1 =="4":
        score += random4
    elif mark1 =="5":
        score += random5
    elif mark1 =="6":
        score += random6
    else:
        score += 0
        
    if mark2 == "1":
        score += random1
    elif mark2 =="2":
        score += random2
    elif mark2 =="3":
        score += random3
    elif mark2 =="4":
        score += random4
    elif mark2 =="5":
        score += random5
    elif mark2 =="6":
        score += random6
    else:
        score += 0
        
    if mark3 == "1":
        score += random1
    elif mark3 =="2":
        score += random2
    elif mark3 =="3":
        score += random3
    elif mark3 =="4":
        score += random4
    elif mark3 =="5":
        score += random5
    elif mark3 =="6":
        score += random6
    else:
        score += 0
    
    return render_template('gmresult.html',mylist=mylist,random1=random1,random2=random2,random3=random3,random4=random4,random5=random5,random6=random6,score=score)
    
if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
