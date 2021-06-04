from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
	path('',views.pdfview,name='home'),
	path('login',views.login,name='login'),
	path('register',views.register,name='register'),
	path('staffregister',views.staffregister,name='staffregister'),
	path('activate/<uidb64>/<token>/',views.activate, name='activate'),
	path('pdfdisplay',views.pdfdisplay,name='pdfdisplay'),
	path('pdfdisplay2',views.pdfdisplay2,name='pdfdisplay2'),
	path('pdfdisplay3',views.pdfdisplay3,name='pdfdisplay3'),
	path('pdfdisplay4',views.pdfdisplay4,name='pdfdisplay4'),
	path('feedback',views.feedback,name='feedback'),
	path('logout',views.logout,name='logout'),
	path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	]