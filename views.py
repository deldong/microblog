#encoding:utf-8
#视图是响应来自网页浏览器的请求的处理器。在 Flask 中，视图是编写成 Python 函数。每一个视图函数是映射到一个或多个请求的 URL。

from app import app

#两个 route 装饰器创建了从网址/以及/index到这个函数的映射。
@app.route('/')
@app.route('/index')
def index():
    return 'hello world!'

