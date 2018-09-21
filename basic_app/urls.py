'''
Created on Aug 31, 2018

@author: gris
'''

from django.conf.urls import url
from basic_app import views
#from Django_Templates.urls import urlpatterns

app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^', views.basic_app_index, name='basic_app_index'),
    
    ]