from django.urls import path

from authapp2 import views

app_name = 'authapp2'


urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.user_list_view, name='user-list-view'),
    path('register/', views.register_view, name='register-name'),
    path('login/', views.login_view, name='login-view'),
    path('logout/', views.logout_view, name='logout-view'),
]