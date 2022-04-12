from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [

    path('', views.index, name="index"),
    path('ask/', views.ask, name="ask"),
    path('question/<int:i>', views.question, name="question"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('tags/<str:tag>', views.tags, name="tags"),
    path('profile/', views.profile, name="profile"),
]