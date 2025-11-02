from django.contrib import admin
from .models import Animatronic


@admin.register(Animatronic)
class AnimatronicAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name', 'description')
    list_filter = ('created', 'updated')


