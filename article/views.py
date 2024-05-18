from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

import core
import core.models
# Create your views here.

class ArticleList(TemplateView):
    template_name = 'article/list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['articles'] = core.models.Article.objects.all()
        return context
    
class UserArticleList(DetailView):
    template_name = 'article/list.html'
    context_object_name = 'author'
    model = core.models.User

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['articles'] = core.models.Article.objects.filter(author=kwargs['object'])
        return context
    
    