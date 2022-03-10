from django.urls import path

from intro import views


urlpatterns = [
    path('home/', views.hello),
    path('home2/', views.hello2),
    path('home3/', views.hello3),
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('<str:name>/', views.name_view),
]
