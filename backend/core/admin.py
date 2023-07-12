from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContacatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'email')