from django.urls import path

from calculator import views

app_name = 'calculator'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('result/<int:res>/', views.result, name='result'),
]