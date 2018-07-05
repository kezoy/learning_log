"""定义learning_logs的URL模式"""

from django.urls import path,re_path

from . import views

urlpatterns = [
	#主页
	path('', views.index, name='index'),
	
	#显示所有主题
	path('topics/', views.topics, name='topics'),
	
	#显示特点主题的详细页面
	re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	
	#用于添加的新主题网页
	path('new_topic/', views.new_topic, name='new_topic'),
	
	#用于添加特定主题的新条目
	re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry, 
			name='new_entry'),
	
	#更改特定主题的特定条目
	re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry, 
			name='edit_entry'),
]
app_name = 'learning_logs'
