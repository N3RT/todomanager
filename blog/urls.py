from django.urls import path

from blog.views import *

urlpatterns = [
    path('hello/', welcome, name = 'welcome'),
]