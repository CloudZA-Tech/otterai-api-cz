from django.urls import path
from otteraiapp import views

urlpatterns = [
    path('login/', views.login),
    path('all_speeches/', views.all_speeches),
    path('speech_id/', views.speech_by_id),
]
