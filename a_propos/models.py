from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models

class AboutUs(models.Model):
    image = models.ImageField(upload_to='about_us/')
    area_title = models.CharField(max_length=200)
    description = models.TextField()
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="AboutUs_createby")
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="AboutUs_updateby")


    class Meta:
        ordering = ('-create_by',)
        verbose_name = 'A propos'
        verbose_name_plural = 'A propos'.upper()
    def __str__(self):
        return self.area_title



class Mission(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priorities = models.TextField()
    image = models.ImageField(upload_to='missions/', null=True, blank=True)
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="missions_created")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="missions_updated")

    class Meta:
        ordering = ('-created_by',)
        verbose_name = 'Missions'
        verbose_name_plural = 'Missions'.upper()

    def __str__(self):
        return self.title


class Volunteer(models.Model):
    full_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    image = models.ImageField(upload_to='volunteers')
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="Volunteer_created")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="Volunteer_updated")

    class Meta:
        ordering = ('-created_by',)
        verbose_name = 'Volontaires'
        verbose_name_plural = 'Volontaires'.upper()

    def __str__(self):
        return self.full_name


class PlusDeStatistiques(models.Model):
    image = models.ImageField(upload_to='plus_de_statistiques/')
    annee_fondation = models.PositiveIntegerField()
    nombre_donateurs = models.PositiveIntegerField()
    nombre_benevoles = models.PositiveIntegerField()
    activites_reussies = models.PositiveIntegerField()
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="PlusDeStatistiques_created")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="PlusDeStatistiques_updated")

    class Meta:
        ordering = ('-created_by',)
        verbose_name = 'PlusDeStatistiques'
        verbose_name_plural = 'PlusDeStatistiques'.upper()

    def __str__(self):
        return f"Plus de Statistiques - Année de fondation : {self.annee_fondation}"

class Partenaire(models.Model):
    image = models.ImageField(upload_to='partenaires/')
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="Partenaire_created")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="Partenaire_updated")

    class Meta:
        ordering = ('-created_by',)
        verbose_name = 'Partenaire'
        verbose_name_plural = 'Partenaire'.upper()

    def __str__(self):
        return self.nom