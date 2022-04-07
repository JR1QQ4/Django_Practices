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

2、把创建的应用的路由添加到 *mysite/urls.py* 中

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













