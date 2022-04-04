from django.urls import path

from viewapp import views

app_name = 'viewapp'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),

    path('template/hello/', views.hello_template, name='hello-template'),
    path('template/hello2/', views.HelloClassView.as_view(), name='hello-template2')
]