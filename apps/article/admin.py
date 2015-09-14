from django.contrib import admin
from .models import Article
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget

__author__ = 'alexy'


class ArticleForm(ModelForm):
    class Meta:
        widgets = {
            'text': RedactorWidget(editor_options={'lang': 'ru'})
        }


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    prepopulated_fields = {"slug": ("title",)}
    form = ArticleForm
    fieldsets = [
        (None, {'classes': ('full-width'),
                'fields': ('title', 'text')}
         ),
        ('SEO', {'fields': ('slug', 'meta_key', 'meta_desc')})
    ]


admin.site.register(Article, ArticleAdmin)
