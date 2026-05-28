from django.contrib import admin

from .models import ContactInfo, ContactMessage


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone1', 'phone2', 'last_update')
    search_fields = ('address', 'email', 'phone1', 'phone2')
    ordering = ('-last_update',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'objet', 'create', 'traite')
    list_filter = ('traite', 'create')
    list_editable = ('traite',)
    search_fields = ('name', 'email', 'phone', 'objet', 'comments')
    readonly_fields = (
        'name', 'email', 'phone', 'objet', 'comments',
        'create', 'last_update', 'created_by', 'updated_by',
    )
    ordering = ('-create',)
    date_hierarchy = 'create'

    fieldsets = (
        (None, {
            'fields': ('traite', 'name', 'email', 'phone', 'objet', 'comments'),
        }),
        ('Suivi', {
            'fields': ('create', 'last_update', 'created_by', 'updated_by'),
            'classes': ('collapse',),
        }),
    )

    @admin.action(description='Marquer comme traité')
    def marquer_traite(self, request, queryset):
        queryset.update(traite=True)

    @admin.action(description='Marquer comme non traité')
    def marquer_non_traite(self, request, queryset):
        queryset.update(traite=False)

    actions = ('marquer_traite', 'marquer_non_traite')
