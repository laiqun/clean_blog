# Clean Blog
---

###  > `FIX`

+ ###### 修改xadmin导入方式(本地包导入)
+ ###### static 引用方式(详见 setting)

### > `Add`

+ ###### 富文本框输入 改为 MarkDown文本输入 
+ ###### 项目部署uwsgi、nginx静态资源代理

### > `BUG`

+ ###### `代码高亮`
+ ###### 可能客户端 archive界面 显示不了那个月的文章，是因为mysql时区的设置问题 可以在 cmd 中
+ ######    cmd 输入 mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -uroot mysql -p 输入密码就可以了
   - ###### 详见[Heading link](https://chowyi.com/Django%E4%BD%BF%E7%94%A8MySQL%E5%90%8E%E7%AB%AF%E6%97%A5%E6%9C%9F%E4%B8%8D%E8%83%BD%E6%8C%89%E6%9C%88%E8%BF%87%E6%BB%A4%E7%9A%84%E9%97%AE%E9%A2%98%E5%8F%8A%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88/ "Heading link")
   
### > `Attaction`

+ ###### 如果本地跑记得把DEBUG 改为TRUE
+ ###### uwsgi 配置文件是那个ini后缀的文件 其他是一些uwsgi产生的文件
+ ###### nginx 配置文件也在uwsgi_cnf里面 直接在 nginx 原配置文件下(/etc/nginx/nginx.conf)的http{}中加入 include nginx_blog.conf 就可以了
---

一个基于Django开发的博客系统:

- Python3.6 和 Django1.10
- MySQL储存方案
- xadmin后台管理
- <s>ckeditor编辑器，图片上传</s>改为 markdown文本 支持富文本的所有输入
- Bootstrap前端模板
- RSS订阅
- 标签分类与日期归档
- 文章评论
- haystack文章内容搜索

Usage:

- 新建虚拟环境

<pre>
git clone https://github.com/helloworld19951213/clean_blog.git
virtualenv --python=<py3path> venv
. venv/bin/activate
pip install -r requirements.txt
</pre>

- 收集静态资源

<pre>
python manage.py collectstatic
</pre>

- 数据库迁移

<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

- 创建管理员
<pre>
python manage.py createsuperuser
</pre>

------
### 首页

![index](/pic/2.png)

### 详情页

![index](/pic/3.png)

### 评论发表

![index](/pic/8.png)

### 归档

![index](/pic/7.png)

### xadmin后台

![index](/pic/5.png)

### ckeditor文章编辑器

![index](/pic/1.png)

### 相关文档
使用haystack这个搜索引擎时，需要多一步操作：

初始化索引数据 python manage.py rebuild_index
使用haystack搜索框架和whoosh后端引擎的博文见：

https://www.cnblogs.com/alexzhang92/p/9529689.html

使用的Blog模板为startbootrap上找到的：

https://startbootstrap.com/template-categories/blogs/

添加文章的后端显示真的很丑，特别是Author这个字段的值显示为 创建时间和修改时间的显示为Null,这种显示非常不友好。

参照下文来修改： https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields
```python
from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('address_report',)

    def address_report(self, instance):
        # assuming get_full_address() returns a list of strings
        # for each line of the address and you want to separate each
        # line by a linebreak
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((line,) for line in instance.get_full_address()),
        ) or mark_safe("<span class='errors'>I can't determine this address.</span>")

    # short_description functions like a model field's verbose_name
    address_report.short_description = "Address"
  ```
  ### 发现markdown全屏编辑状态还会显示其他amdin控件的bug，需要调整前端
