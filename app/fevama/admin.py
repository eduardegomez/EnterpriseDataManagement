from django.contrib import admin

from .models import *
from django.utils.translation import *
from django.shortcuts import render, redirect

# Register your models here.

# CONTACT
class ContactAdmin(admin.ModelAdmin):
    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = gettext_lazy('Delete')

    def get_queryset(self, request):
        qs = super(ContactAdmin, self).get_queryset(request)
        return qs

    def add_view(self, request):
        return redirect('/app/notify/new')

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super(ContactAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Contact,ContactAdmin)