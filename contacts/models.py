from django.conf import settings
from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="ContactInfo_created")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="ContactInfo_updated")

    class Meta:
        ordering = ('-created_by',)
        verbose_name = 'ContactInfo'
        verbose_name_plural = 'ContactInfo'.upper()

    def __str__(self):
        return self.address



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    objet = models.CharField(max_length=200)
    comments = models.TextField()
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="ContactMessage_created")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name="ContactMessage_updated")

    class Meta:
        ordering = ('-created_by',)
        verbose_name = 'ContactMessage'
        verbose_name_plural = 'ContactMessage'.upper()

    def __str__(self):
        return self.name