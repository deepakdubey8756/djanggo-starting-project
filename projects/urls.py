from django.contrib import admin
from django.urls import path, include
from projects import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:pk>/", views.project_detail, name="project_details")
]
