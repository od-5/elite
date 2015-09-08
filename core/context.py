from .models import Setup
__author__ = 'alexy'


def site_setup(request):
    try:
        qs = Setup.objects.all().first()
    except:
        qs = None
    return {
        'setup': qs,
    }
