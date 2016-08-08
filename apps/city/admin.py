# coding=utf-8
from django.contrib import admin
from django import forms
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from .models import City, CityArea, CityStreet, CityHouse

__author__ = 'alexy'


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'manager', 'email', 'phone', 'coord_x', 'coord_y')
    prepopulated_fields = {'slug': ('name',)}

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return City.objects.all()
        else:
            return City.objects.filter(city__manager=user)


class AreaForm(forms.ModelForm):
    class Meta:
        model = CityArea
        fields = '__all__'


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('city',)

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return CityArea.objects.all()
        else:
            return CityArea.objects.filter(city__manager=user)

    def get_form(self, request, obj=None, **kwargs):
        form = AreaForm
        if not request.user.is_superuser:
            form.base_fields['city'].queryset = City.objects.filter(manager=request.user)
            form.base_fields['city'].initial = City.objects.filter(manager=request.user).first()
        return form


class StreetForm(forms.ModelForm):
    class Meta:
        model = CityStreet
        fields = '__all__'


class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'area')
    list_filter = ('city', 'area')

    def get_form(self, request, obj=None, **kwargs):
        form = StreetForm
        if not request.user.is_superuser:
            form.base_fields['city'].queryset = City.objects.filter(manager=request.user)
            form.base_fields['city'].initial = City.objects.filter(manager=request.user).first()
            form.base_fields['area'].queryset = CityArea.objects.filter(city__manager=request.user)
        return form

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return CityStreet.objects.all()
        else:
            return CityStreet.objects.filter(city__manager=user)


class HouseForm(forms.ModelForm):
    class Meta:
        model = CityHouse
        fields = '__all__'


class HouseAdmin(admin.ModelAdmin):
    list_display = ('number', 'city', 'area', 'street', 'coord_x', 'coord_y')
    list_filter = ('city', 'area', 'street')

    def get_form(self, request, obj=None, **kwargs):
        form = HouseForm
        if not request.user.is_superuser:
            form.base_fields['city'].queryset = City.objects.filter(manager=request.user)
            form.base_fields['city'].initial = City.objects.filter(manager=request.user).first()
            form.base_fields['area'].queryset = CityArea.objects.filter(city__manager=request.user)
            form.base_fields['street'].queryset = CityStreet.objects.filter(city__manager=request.user)
        return form

    def get_queryset(self, request):
        user = request.user
        if user.is_superuser:
            return CityHouse.objects.all()
        else:
            return CityHouse.objects.filter(city__manager=user)


admin.site.register(City, CityAdmin)
admin.site.register(CityArea, AreaAdmin)
admin.site.register(CityStreet, StreetAdmin)
admin.site.register(CityHouse, HouseAdmin)
