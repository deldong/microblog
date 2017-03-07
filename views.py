#encoding:utf-8
#视图是响应来自网页浏览器的请求的处理器。在 Flask 中，视图是编写成 Python 函数。每一个视图函数是映射到一个或多个请求的 URL。

from app import app
from flask import render_template

#两个 route 装饰器创建了从网址/以及/index到这个函数的映射。
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Delon'} #fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title = 'Home',
                           user = user,
                           posts = posts
                           )
"""
为了渲染模板，我们必须从 Flask 框架中导入一个名为 render_template 的新函数。此函数需要传入模板名以及一些模板变量列表，返回一个所有变量被替换的渲染的模板。

在内部，render_template 调用了 Jinja2 模板引擎，Jinja2 模板引擎是 Flask 框架的一部分。Jinja2 会把模板参数提供的相应的值替换了 {{...}} 块。

"""

