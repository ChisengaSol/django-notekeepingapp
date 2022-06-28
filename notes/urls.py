from django.urls import path
from django.conf.urls import url,include
from . import views
import django.contrib.auth.views as auth_views

app_name='notes'

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='notes/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='notes/loggedout.html'),name='logout'),
    path('home/',views.home_page,name='home_page'),
    path('update/<int:id>/',views.update,name='update'),
    path('register/',views.register,name='register'),
    path('settings/',views.settings,name='settings'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('add-programming-language/',views.add_proglanguage,name='add-programming-language'),
]