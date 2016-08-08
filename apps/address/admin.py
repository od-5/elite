from django.contrib import admin
from django import forms
from apps.city.models import City
from .models import Address, AddressItem

__author__ = 'alexy'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class AddressItemForm(forms.ModelForm):
    class Meta:
        model = AddressItem
        fields = '__all__'


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'pic', )
    list_filter = ('city', )

    def get_queryset(self, request):
        qs = Address.objects.all()
        user = request.user
        if user.is_superuser:
            return qs
        else:
            return qs.filter(city__manager=user)

    def get_form(self, request, obj=None, **kwargs):
        form = AddressForm
        if not request.user.is_superuser:
            form.base_fields['city'].queryset = City.objects.filter(manager=request.user)
            form.base_fields['city'].initial = City.objects.filter(manager=request.user).first()
        return form


class AddressItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'pic')

    def get_queryset(self, request):
        qs = AddressItem.objects.all()
        user = request.user
        if user.is_superuser:
            return qs
        else:
            return qs.filter(address__city__manager=user)

    def get_form(self, request, obj=None, **kwargs):
        form = AddressItemForm
        if not request.user.is_superuser:
            form.base_fields['address'].queryset = Address.objects.filter(city__manager=request.user)
        return form


admin.site.register(Address, AddressAdmin)
admin.site.register(AddressItem, AddressItemAdmin)
