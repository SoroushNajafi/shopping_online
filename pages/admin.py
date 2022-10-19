from django.contrib import admin

from .models import Subscribe, Contact


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Contact)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
