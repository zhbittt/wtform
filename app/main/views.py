from flask import request,redirect,render_template,session,flash,get_flashed_messages
from . import main
from ..db import POOL
from ..Form.forms import LoginForm
from ..Form.forms import RegisterForm
import functools

def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        if session.get("user_info") is None and request.path !='/login' and request.path !='/register':
            print("login")
            return redirect("/login")
        return func(*args,**kwargs)
    return inner

@main.route('/login',methods=['GET','POST'])
def login():

    # ((1, 'pythonwusir', 'pythonwusirQ1`', 'WE@QQ.COM', 1, 1, 1, 1),) <class 'tuple'>
    if request.method =="GET":
        msg=get_flashed_messages()
        form = LoginForm()
        return render_template("login.html",form =form,msg=msg)
    else:
        form=LoginForm(formdata=request.form)
        # {'name': 'wqeqeqwe', 'pwd': 'qweqweqwe', 'pwd_confirm': 'qweqweqwe', 'email': 'qwe@123.com', 'gender': 1,
         # 'city': 'sh', 'hobby': [1], 'favor': [3]}
        if form.validate():
            # qqqqQQQ1111... // /?
            print(form.data, type(form.data))
            name = form.data.get("name",None)
            pwd = form.data.get("pwd",None)
            email = form.data.get("pwd",None)
            gender = form.data.get("pwd",None)
            city = form.data.get("pwd",None)
            hobby = form.data.get("pwd",None)
            favor = form.data.get("pwd",None)

            conn = POOL.connection()
            cursor = conn.cursor()

            sql = 'insert into User (name,pwd,email,gender,city,hobby,favor) values("%s","%s","%s","%s","%s","%s");'
            cursor.execute(sql,())
            result = cursor.fetchall()
            print(result, type(result))
            conn.close()
            if result:
                session["user_info"]="luo"
                return redirect('/index')
        return render_template("login.html",form =form)


@main.route("/index",methods=['GET',])
@auth
def index():
    return render_template("index.html")

@main.route("/register",methods=["GET","POST"])
@auth
def register():
    if request.method=="GET":
        form = RegisterForm()
        return render_template("register.html",form=form)
    else:
        form = RegisterForm(formdata=request.form)
        if form.validate():
            print(form.data)
            conn = POOL.connection()
            cursor = conn.cursor()
            cursor.execute('select * from User where name=%s and pwd=%s' % (name, pwd))
            result = cursor.fetchall()
            print(result, type(result))
            conn.close()
            flash("您已注册成功，请登录！")

            return redirect("/login")
        return render_template("register.html", form=form)