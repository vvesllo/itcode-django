from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

import core
# Create your views here.

def user_articles(request, user_pk):
    articles = core.models.Article.objects.filter(author__pk=user_pk)
    return render(request, 'article/list.html', {'articles': articles, 'author': core.models.User.objects.get(pk=user_pk)})

class ArticleList(TemplateView):
    template_name = 'article/list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        articles = core.models.Article.objects.all()
        context = super().get_context_data(**kwargs)
        context['articles'] = articles
        return context