from django.conf import settings
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre")
    resume = models.TextField(verbose_name="Résumé")
    contenu = models.TextField(blank=True, verbose_name="Contenu")
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="Image")
    date_pub = models.DateTimeField(null=True, blank=True, verbose_name="Date de publication")
    auteur = models.CharField(max_length=100, verbose_name="Auteur")
    tags = models.CharField(max_length=200, blank=True, verbose_name="Tags")
    create = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    last_update = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="articles_created",
        verbose_name="Créé par"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="articles_updated",
        verbose_name="Mis à jour par"
    )
    is_favorite = models.BooleanField(default=False, verbose_name="Favori")

    def __str__(self):
        return self.titre

    def get_previous_by_date_pub(self):
        if self.date_pub:
            return Article.objects.filter(date_pub__lt=self.date_pub, date_pub__isnull=False).order_by('-date_pub').first()
        return None

    def get_next_by_date_pub(self):
        if self.date_pub:
            return Article.objects.filter(date_pub__gt=self.date_pub, date_pub__isnull=False).order_by('date_pub').first()
        return None

    class Meta:
        ordering = ['-date_pub']
        verbose_name = "Article"
        verbose_name_plural = "Articles"