from django.contrib import admin
from django.urls import path

from article import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='index'),
    path('user/<int:pk>', views.UserArticleList.as_view(), name='user'),
]
