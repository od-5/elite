from .models import FAQ

__author__ = 'alexy'


def faq_list(request):
    qs = FAQ.objects.all()
    return {
        'FAQ_MENU': qs,
    }
