from django.contrib import admin
from django.utils.html import format_html
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_pub', 'tags', 'is_favorite', 'resume_preview', 'image_preview', 'created_by', 'last_update')
    list_display_links = ('titre',)
    list_filter = ('auteur', 'date_pub', 'tags', 'is_favorite', 'created_by', 'updated_by')
    search_fields = ('titre', 'resume', 'contenu', 'auteur', 'tags')
    list_per_page = 20
    fields = ('titre', 'resume', 'contenu', 'image', 'auteur', 'tags', 'is_favorite', 'created_by', 'updated_by', 'date_pub', 'create', 'last_update')
    readonly_fields = ('create', 'last_update')

    def resume_preview(self, obj):
        return obj.resume[:100] + '...' if len(obj.resume) > 100 else obj.resume
    resume_preview.short_description = 'Aperçu du résumé'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = 'Image'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)