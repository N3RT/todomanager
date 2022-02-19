from django.urls import path

from blog.views import *

urlpatterns = [
    path('', startPage, name='startPage'),
    path('blog/', blog, name='blog'),
    path('feedback/', feedback, name='feedback'),
]
