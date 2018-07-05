"""为应用程序users定义URL模式"""

from django.urls import path,re_path
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	#登录界面
	path('login/', login, {'template_name':'users/login.html'},
		name='login'),
	#注销登录
	path('logout/', views.logout_view, name='logout'),
	#注册用户
	path('register/', views.register, name='register'),
]
app_name = 'users'
