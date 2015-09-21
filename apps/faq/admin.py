# coding=utf-8
from django.contrib import admin
from .models import FAQ
from django.forms import ModelForm, Textarea
from suit_redactor.widgets import RedactorWidget

__author__ = 'alexy'


class FAQForm(ModelForm):
    class Meta:
        widgets = {
            'question': Textarea(attrs={'style': 'width:98%'}),
            'answer': RedactorWidget(editor_options={'lang': 'ru'}),
        }


class FAQAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'slug', 'created')
    form = FAQForm
    fieldsets = [
        (u'Вопрос', {'classes': ('full-width',),
                'fields': ('question',)}
         ),
        (u'Ответ', {'classes': ('full-width',),
                'fields': ('answer',)}
         ),
        ('SEO', {'classes': ('collapse',),
                 'fields': ('slug', 'meta_key', 'meta_desc')})
    ]


admin.site.register(FAQ, FAQAdmin)
