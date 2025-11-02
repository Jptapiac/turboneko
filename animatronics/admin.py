from django.contrib import admin
from .models import Animatronic, Category, Manufacturer, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name', 'description')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website')
    search_fields = ('name', 'country')
    list_filter = ('country',)


@admin.register(Animatronic)
class AnimatronicAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'manufacturer', 'created')
    list_filter = ('category', 'manufacturer', 'created', 'stock')
    search_fields = ('name', 'description')
    raw_id_fields = ('category', 'manufacturer')
    list_editable = ('price', 'stock')
    readonly_fields = ('created', 'updated')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'img')
        }),
        ('Business Information', {
            'fields': ('price', 'stock', 'category', 'manufacturer')
        }),
        ('Timestamps', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        })
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'animatronic', 'rating', 'created')
    list_filter = ('rating', 'created')
    search_fields = ('comment', 'user__username', 'animatronic__name')
