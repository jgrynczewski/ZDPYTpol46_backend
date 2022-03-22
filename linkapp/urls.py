from django.urls import path

from linkapp import views

urlpatterns = [
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/<str:param>/', views.third, name='third'),
]