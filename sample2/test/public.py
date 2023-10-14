from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'sub' in request.form:
		uname=request.form['username']
		password=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		print(res)
		if res:
			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.adminhome'))



	return render_template('login.html')

@public.route('/register',methods=['get','post'])
def register():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		address=request.form['address']
		mail=request.form['mail']
		genders=request.form['gender']
		uname=request.form['uname']
		password=request.form['password']
		q="insert into login values(NULL,'%s','%s','user')"%(uname,password)
		loginid=insert(q)
		q="insert into register values(NULL,'%s','%s','%s','%s','%s','%s')"%(loginid,fname,lname,address,mail,genders)
		insert(q)
		return redirect(url_for('public.register'))
	return render_template('register.html')



