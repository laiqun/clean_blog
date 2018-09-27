import xadmin
from mdeditor.widgets import MDEditorWidget
from xadmin import views

from .models import Post, Category, Tag
from django.db import models


class GlobalSetting(object):
    site_title = 'clean blog v.1.0'
    site_footer = 'my blog'


xadmin.site.register(views.CommAdminView, GlobalSetting)


class PostAdmin(object):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}

    }
    list_display = (
        'title',
        # 'author',
        # 'content',
        'summary',
        'created_time',
        'category',
    )
    readonly_fields = [
        'author',
        'modify_time',
        'created_time',
    ]
    style_fields = {"content": "ueditor"}

    def save_models(self):
        user = self.request.user
        obj = self.new_obj
        obj.author = user
        obj.save()


# 注册到后台
xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category)
xadmin.site.register(Tag)
