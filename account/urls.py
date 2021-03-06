from django.conf.urls import url
from . import views

urlpatterns = [
	# previous login view
	# url(r'^login/$', views.user_login, name='login'),

	# login / logout urls
	url(r'^login/$',
		'django.contrib.auth.views.login',
		name='login'),
	url(r'^logout/$',
		'django.contrib.auth.views.logout',
		name='logout'),
	url(r'^logout-then-login/$',
		'django.contrib.auth.views.logout_then_login',
		name='logout_then_login'),

	# Dashboard view
	url(r'^$', views.dashboard, name='dashboard'),
]