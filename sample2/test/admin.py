from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('admin.html')

@admin.route('/adminmanagecatagory',methods=['get','post'])
def adminmanagecatagory():
	if 'submit' in request.form:
		catagoryname=request.form['categoryname']
		q="insert into category values(NULL,'%s')"%(catagoryname)
		insert(q)
		return redirect(url_for('admin.adminmanagecatagory'))
	data={}
	q="select * from category"
	res=select(q)
	print(res)
	data['cat']=res

	return render_template('admin managecatagory.html',data=data)

