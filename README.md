## Django 项目

基于 Python 3.8.10 + Django 3.2.12

### 目录结构

#### 第一步、项目的创建与运行

1、脚手架初始化项目 `$ django-admin startproject mysite`：

- 最外层的 *mysite/* 根目录只是你项目的容器， 根目录名称对 Django 没有影响，你可以将它重命名为任何你喜欢的名称
- *manage.py*: 一个让你用各种方式管理 Django 项目的命令行工具
- 里面一层的 *mysite/* 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 mysite.urls)
- *mysite/__init__.py*：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包
- *mysite/settings.py*：Django 项目的配置文件
- *mysite/urls.py*：Django 项目的 URL 声明，就像你网站的“目录”
- *mysite/asgi.py*：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口
- *mysite/wsgi.py*：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口

2、运行 `$ python .\manage.py runserver 0.0.0.0:8000`，远程访问需配置 *mysite/settings.py* 文件 `ALLOWED_HOSTS = ['*']`


#### 第二步、应用的创建和使用

1、创建应用 `$ python .\manage.py startapp DBCompare`:

- *DBCompare/admin.py*: 后台
- *DBCompare/apps.py*: 应用
- *DBCompare/models.py*: 数据库操作
- *DBCompare/tests.py*: 测试
- *DBCompare/views.py*: 视图
- *DBCompare/migrations*: 数据库迁移

2、创建 *urls.py* 文件，把创建的应用的路由添加到 *mysite/urls.py* 中

3、非必要步骤，数据库配置：

- ENGINE -- 可选值有: 'django.db.backends.sqlite3'，'django.db.backends.postgresql'，'django.db.backends.mysql'，或 'django.db.backends.oracle'。
    - MS SQL SERVER 需要安装插件 `$ pip install django-mssql-backend`
    - MySQL 只需配置即可

```python
# MS SQL SERVER 配置
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'mydb',
        'USER': 'user@myserver',
        'PASSWORD': 'password',
        'HOST': 'myserver.database.windows.net',
        'PORT': '',

        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',  # 可选 "SQL Server Native Client 11.0", "FreeTDS"
        },
    },
}

# set this to False if you want to turn off pyodbc's connection pooling
DATABASE_CONNECTION_POOLING = False
```

```python
# MySQL 配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'mydatabaseuser',
        'NAME': 'mydatabase',
        'TEST': {
            'NAME': 'mytestdatabase',
        },
    },
}
```

#### 第三步、项目的模型

0、直接使用 *sqlite3*，[参考文档](https://blog.csdn.net/wzzzj/article/details/112789956)，步骤如下:

- 在 *settings.py* 中配置 *INSTALLED_APPS*
- 创建模型，编辑 *myapp/models.py* 文件
- 将自定义的应用程序加入到后台管理，编辑 *myapp.admin.py* 文件
- 运行命令 `$ python manage.py makemigrations`，将你对 models.py 文件中的改动保存到当前目录中一个叫 migrations 的文件夹中，但还未同步到数据库
- 运行命令 `$ python manage.py migrate`，将改动同步到数据库
- 运行命令 `$ python manage.py createsuperuser`，创建Web后台的用户名和密码
- 启动后台 `$ python manage.py runserver`，打开 *http://127.0.0.1:8000/admin*

1、连接 MySQL 数据库设置: `$ pip install MySQL`，在 *settings.py* 中配置 *DATABASES*

2、创建模型，编辑 *myapp/models.py* 文件

```python
# myapp/models.py

from django.db import models

# Create your models here.
class Stu(models.Model):
    '''自定义USER表对应的Model类'''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    password = models.CharField()
    email = models.CharField()

    def __str__(self) -> str:
        return "%d, %s, %s" % (self.id, self.name, self.email)
    
    # 自定义对应的表名，默认表名: myapp_stu
    class Meta:
        db_table = "stu"
```

3、在 *settings.py* 中配置 *INSTALLED_APPS*

```python
# mysite/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',  # 或者直接写 mysapp
]
```

4、使用：

- 第一种方法：`$ python manage.py shell` 交互式
- 第二种方法：一般在试图 *myapp/views.py* 中使用 

```shell
$ python manage.py shell
>> from myapp.models import Stu
>> mod = Stu.objects
>> lists = mod.all()  # 获取所有信息
>> for v in lists:
...    print(v)
>> mod.get(id=1)  # 获取指定行的信息
```

```python
# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Stu

# Create your views here.
def index(request):
    return HttpResponse('My App！')

def abc(request):
    lists = Stu.objects.all()  # 获取所有信息
    for v in lists:
        print(v)
    print(Stu.objects.get(id=6))
    return HttpResponse('abc！')

```

#### 第四步、启动网站 admin 管理

1、数据迁移: `$ puthon manage.py migrate`，执行之后会自动创建一些表；然后创建管理员用户: `$ python manage.py createsuperuser`，进入提示操作

```python
# mysite/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',  # 管理网站
    'django.contrib.auth',  # 认证系统
    'django.contrib.contenttypes',  # 内容类型的框架
    'django.contrib.sessions',  # 会话框架
    'django.contrib.messages',  # 消息框架
    'django.contrib.staticfiles',  # 管理静态文件的框架
    'myapp.apps.MyappConfig',  # 或者直接写 mysapp
]
```

2、启动服务，管理员站点被激活: `$ python manage.py runserver`

3、设置时区和语言，编辑 *mysite/settings.py* 文件

```python
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

4、将自定义的应用程序加入到后台管理，编辑 *myapp.admin.py* 文件

```python
# myapp.admin.py

from django.contrib import admin
from myapp.models import Stu

# Register your models here.
admin.site.register(Stu)
```

5、更加深入的后台管理设置，编辑 *myapp/models.py* 文件，编辑 *myapp/admin.py* 文件

```python
# myapp/models.py

from django.db import models

# Create your models here.
class Stu(models.Model):
    '''自定义USER表对应的Model类'''
    id = models.AutoField('Id', primary_key=True)
    name = models.CharField('Name', max_length=16)
    password = models.CharField()
    email = models.CharField('Email')

    def __str__(self) -> str:
        return "%d, %s, %s" % (self.id, self.name, self.email)
    
    # 自定义对应的表名，默认表名: myapp_stu
    class Meta:
        db_table = "stu"
        verbose = '浏览用户信息'
        verbose_name_plural = '用户信息管理'
```

```python
# myapp.admin.py

from django.contrib import admin
from myapp.models import Stu

# Register your models here.

# Stu模型的管理器（装饰器写法）
@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    # 设置要显示在列表中的内容
    list_display = ('id', 'name', 'email')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name', 'email')

    # 设置每页显示多少条记录，默认是100条
    list_per_page = 10

    # 设置默认排序字段，负号表示降序排序，-id
    ordering = ('id',)

    # 设置默认可编辑字段
    # list_eaitable = ['name', 'email']
```

### URL路由配置

#### Django框架是如何处理请求

1. 首先确定要使用的根 URLconf 模块，通过 ROOT_URLCONF 来设置，在 settings.py 文件中。但是如果传入 HttpRequest 对象具有 urlconf 属性
（有中间件设置）， 则其值将用于替换 ROOT\_URLCONF 设置
2. Django 加载 Python 模块并查找该变量 urlpatterns，它是 django.urls.path() 和（或） django.urls.re_path() 实例的序列(sequence)
3. Django 按顺序运行每个 URL 模式，并在匹配所请求的 URL 的第一个 URL 中停止
4. 一旦正则表达式匹配，Django 将导入并调用给定的视图，这是一个简单的 Python函数（或基于类的试图）。该试图会获得如下参数：
   - 一个 HttpRequest 实例
   - 如果匹配的正则表达式没有返回任何命名组，那么来自正则表达式的匹配将作为位置参数提供
   - 关键字参数由正则表达式匹配的任何命名组组成，由可选 kwargs 参数中指定的任何参数覆盖。django.url.path(\)、django.urls.re_path(\)
5. 如果没有正则表达式匹配，或者在此过程中的任何一点出现异常，Django 将调用适当的错误处理视图


#### URLconf 配置

以下是一个 URLconf 实例：
```python
from django.urls import path
from . import views

# <> 用于从 URL 中捕获一个值，称为路径转换器，可以有的类型：str、int、slug、uuid、path
urlpatterns = [
    path('article/2003/', views.special_case_2003),
    path('articles/<int:year>', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>', views.article_detail)
]
```

通过浏览器访问服务：
```text
通过浏览器访问服务 127.0.0.1:8000/abc  -->  root url(根路由)  -->  加载子路由(myweb/urls.py)
    -->  正则匹配访问的路径(path)  -->  试图函数(views.index)
    --> views.py index() 相应内容
```

使用正则表达式：
```python
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('article/2003/', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w+])/$', views.article_detail)
]
```

#### 错误处理

关于 404 错误：

- 在模板目录中创建一个 404.html 的页面
- 在配置文件中 `settings.py` 配置 `DEBUG=False`
- 在配置文件中 `settings.py` 配置 `TEMPLATES = [{'DIRS': [os.path.join(BASE_DIR, 'templates')]}]`
- 同事需要在项目的根目录下创建文件夹 templates，并且在此目录下创建一个 404.html 文件
- 在出现 404 的情况时，自动寻找 404 页面
- 也可以在视图函数中手动报出 404 错误，带提示信息

在视图函数中也可以指定返回一个 404：
```text
注意 Http404 需要在 django.http 的模块中引入
raise Http404('404 Not Found.')
```

在模板中 404.HTML：
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <main>
        <h2>404 not found</h2>
        <h3>{{ exception }}}</h3>
    </main>
</body>
</html>
```

### Django 的 Model 模型层

模型介绍：

- 模型时我们项目中的数据信息源，它包含着储存数据的必要字段和行为
- 通常，每个模型对应数据库中的一张表，每个属性对应一个字段
- 每个模型都是 django.db.models.Model 的一个 Python 子类
- Django 提供一套自动生成的用于数据库访问的 API
- 模型与数据库的关系是 ORM 关系（对象-关系-映射）
- 为什么要用模型？Model 是 MVC 框架中重要的一部分，负责在数据库中存取数据，它实现了数据模型与数据库的解耦，即不需要依赖于特定的数据库，通过简单的配置就可以轻松更换数据库

Model 的开发流程：
1. 在应用的 models.py 中定义模型类，要求继承子 models.Model
2. 把应用加入到项目 settings.py 配置文件的 INSTALLED_APPS 项中
3. 生成迁移文件 `$ python manage.py makemigrations`
4. 执行迁移 `python manage.py migrate`
5. 使用模型类进行 CRUD 操作

#### 定义 Model 模型

- 在模型中定义属性，会生成表中的字段
- Django 根据属性的类型确定以下信息：
  - 当前选择的数据库支持字段的类型
  - 渲染管理表单时使用的默认 html 控件
  - 在管理站点最低限度的验证
- Django 会为表增加自动增长的主键列，每个模型只能有一个主键列
- 属性命名限制：不能时 Python 的保留关键字；由于 Django 的查询方式，不允许使用连续的下划线

Model 模型的实例：

- 模型实例对象是通过 objects 属性获取，即 Django 为模型类提供的管理器
  - objects：是 Manager 类型的对象，用于与数据库进行交互
- 实例的方法：
  - `__str__(self)`：重写 object 方法，此方法在将对象转换成字符串时会被调用
  - `save()`：将模型对象保存到数据表中
  - `delete()`：将模型对象从数据表中删除

字段类型：

- AutoField
- BooleanField
- NullBooleanField
- CharField
- TextField
- IntegerField
- DecimalField
- FloatField
- DateField
- TimeField
- DateTimeField
- FileField
- ImageField

#### 开发前的配置

1、创建数据库和表（若是执行表迁移，可跳过下面操作）

- 进入 MySQL 数据库创建数据库：mytest
- 进入数据库创建数据表：myapp_users，并添加数据

```mysql
CREATE TABLE `myapp_users` (
    `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(32) NOT NULL ,
    `age` tinyint(3) unsigned NOT NULL DEFAULT `20`,
    `phone` varchar(16) DEFAULT NULL,
    `addtime` datetime(6) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8
```

2、创建项目 myweb 和应用 demo2

```text
$ django-admin startproject mysite
$ python manage.py startapp demo2
$ mkdir templates
$ mkdir templates/demo2
```

3、执行数据库连接配置，网站配置：

- 编辑 settings.py 文件，配置数据库连接

```text
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demo2'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [pathlib.Path.joinpath(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'NAME': 'demo2',  # 数据库的名称
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}
```

#### 开发流程

1、在 models.py 中定义模型类，要求继承自 models.Model

```python
from django.db import models
from datetime import datetime


# Create your models here.
class Users(models.Model):
    # id = models.AutoField(primary_key=True)  # 主键可省略不屑
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    addtime = models.DateTimeField(default=datetime.now)


# class Meta:
#     db_table = "demo2_user"  # 指定表名，默认就是app的名称+'_'+小写类名
```

2、把应用加入到 settings.py 文件的 installed_app 项

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demo2'
]
```

3、生成迁移文件：`$ python manage.py makemigrations`，多了一个文件 demo2\migrations\0001_initial.py

4、执行迁移：`$ python manage.py migrate`

### Django 的 View 视图层

见项目 demo3

### Django 的模板层












 