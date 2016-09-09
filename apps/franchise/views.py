# coding=utf-8
from django.views.generic import TemplateView
from .models import Block1, Block2, Client, Block3, Block4, Block5, Block6

__author__ = 'alexey'


class FranchiseView(TemplateView):
    template_name = 'franchise.html'

    def get_context_data(self, **kwargs):
        context = super(FranchiseView, self).get_context_data()
        block1 = Block1.objects.all()
        block2 = Block2.objects.all()
        block3 = Block3.objects.all()
        block4 = Block4.objects.all()
        block5 = Block5.objects.all()
        block6 = Block6.objects.all()
        client_qs = Client.objects.all()
        context.update({
            'block1': block1,
            'block2': block2,
            'block3': block3,
            'block4': block4,
            'block5': block5,
            'block6': block6,
            'client_list': client_qs,
        })
        return context
