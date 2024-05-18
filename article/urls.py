from django.contrib import admin
from django.urls import path

from article import views

urlpatterns = [
    path('', views.article_list, name='index'),
    path('user/<int:user_pk>', views.ArticleList().as_view(), name='user'),
]
