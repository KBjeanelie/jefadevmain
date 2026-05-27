from django.contrib import admin
from .models import CarouselItemBannier, Testimonial

@admin.register(CarouselItemBannier)
class CarouselItemBannierAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'create', 'last_update', 'create_by', 'update_by')
    search_fields = ('title', 'subtitle', 'description')
    list_filter = ('create', 'last_update', 'create_by')
    ordering = ('-create',)
    date_hierarchy = 'create'
    readonly_fields = ('create', 'last_update')
    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'subtitle', 'description')
        }),
        ('Bouton', {
            'fields': ('button_text', 'button_url'),
            'classes': ('collapse',),
        }),
        ('Métadonnées', {
            'fields': ('create', 'last_update', 'create_by', 'update_by'),
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status', 'create', 'last_update', 'create_by', 'update_by')
    search_fields = ('full_name', 'status', 'message')
    list_filter = ('create', 'status', 'create_by')
    ordering = ('-create',)
    date_hierarchy = 'create'
    readonly_fields = ('create', 'last_update')
    fieldsets = (
        (None, {
            'fields': ('full_name', 'status', 'message')
        }),
        ('Métadonnées', {
            'fields': ('create', 'last_update', 'create_by', 'update_by'),
        }),
    )
