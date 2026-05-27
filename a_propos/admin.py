from django.contrib import admin
from .models import AboutUs, Mission, Volunteer, PlusDeStatistiques, Partenaire


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('area_title',)
    search_fields = ('area_title',)
    ordering = ('-create',)


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'create', 'last_update', 'created_by', 'updated_by')
    search_fields = ('title',)
    ordering = ('-create',)


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status')
    search_fields = ('full_name', 'status')
    ordering = ('-create',)


@admin.register(PlusDeStatistiques)
class PlusDeStatistiquesAdmin(admin.ModelAdmin):
    list_display = ('annee_fondation', 'nombre_donateurs', 'nombre_benevoles', 'activites_reussies')
    search_fields = ('annee_fondation',)
    ordering = ('-create',)


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
    ordering = ('-create',)



