from django.urls import path

from formapp2 import views

app_name = "formapp2"

urlpatterns = [
    path('list/', views.message_list, name='message-list'),
    path('1/', views.contact1, name='contact1')
]