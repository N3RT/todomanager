from django.urls import path

from TaskManager.views import test0

urlpatterns = [
    path('test/', test0, name = 'test'),
]