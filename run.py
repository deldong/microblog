#encoding:utf-8
#!flask/bin/python
from app import app
app.run(debug = True)

#这个脚本简单地从我们的 app 包中导入 app 变量并且调用它的 run 方法来启动服务器。请记住 app 变量中含有我们在之前创建的 Flask 实例。
