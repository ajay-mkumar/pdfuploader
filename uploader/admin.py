from django.contrib import admin
from .models import EbookModel,EbookModel2,EbookModel3,EbookModel4,FeedBack,User,teacher,student

from django.conf.urls import url
from django.contrib import admin

admin.site.site_header = 'AVC admin'
admin.site.site_title = 'AVC admin'

admin.site.register(User)
admin.site.register(teacher)
admin.site.register(student)
admin.site.register(EbookModel)
admin.site.register(EbookModel2)
admin.site.register(EbookModel3)
admin.site.register(EbookModel4)
admin.site.register(FeedBack)