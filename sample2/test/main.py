from flask import *
from public import public
from admin import admin

app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
# app.register_blueprint(admin,url_prefix='/admin')

app.run(debug=True,port=5021)