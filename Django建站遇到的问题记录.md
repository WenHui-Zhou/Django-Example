Django建站遇到的问题记录
===============

 - 提交表单时遇到`csrf verification failed. request aborted.` csrf认证拒绝的问题

解决方法：

> 检查settings中的MIDDLEWARE是否有：`'django.middleware.csrf.CsrfViewMiddleware',` 没有则添上，同时在表单调用的函数上面加上修饰符：`@csrf_exempt` 这个修饰符需要在文件头引入：`from django.views.decorators.csrf import csrf_exempt`

 - 关于html引用css，js的问题

> 在html所在应用下建一个static文件夹。static文件夹中有css,js文件夹。将相应文件放到这里。
> 然后在settings文件的末尾加上：
> `
STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
STATICFILES_DIRS = (
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/')),
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/'))
)`
html文件引用使用：
`<link rel="stylesheet" type="text/css" href="../static/css/base.css" />` 即可

 - 关于表单如何调用函数：

> 所有的函数需要在urls文件中配置相应的访问链接，有了访问链接就可以访问了。
> urls中：
> ` url(r'^loginCheck/',Login_views.loginCheck,name='loginCheck'),`
> 调用：
> `<form action="/loginCheck/" method="post" >`


