from django.contrib import admin
from .models import FileReview, TextReview

__author__ = 'alexy'


class FileReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'pic', )
    # list_filter = ('city',)

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return FileReview.objects.all()
        else:
            return FileReview.objects.filter(city__manager=user)


class TextReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'city', 'pic')
    # list_filter = ('city',)

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return TextReview.objects.all()
        else:
            return TextReview.objects.filter(city__manager=user)


admin.site.register(FileReview, FileReviewAdmin)
admin.site.register(TextReview, TextReviewAdmin)
