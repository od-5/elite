from .models import Article

__author__ = 'alexy'


def article_list(request):
    qs = Article.objects.all()
    return {
        'ARTICLE_MENU': qs,
    }
