from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

# Create your models here.
class CarouselItemBannier(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    button_text = models.CharField(max_length=50, blank=True)
    button_url = models.URLField(blank=True)
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="CarouselItemBannier_createby")
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="CarouselItemBannier_updateby")

    class Meta:
        ordering = ('-create_by',)
        verbose_name = 'CarouselBannier'
        verbose_name_plural = 'CarouselBannier'.upper()

    def __str__(self):
        return self.title



class Testimonial(models.Model):
    full_name = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    message = models.TextField()
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="Testimonial_createby")
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="Testimonial_updateby")

    class Meta:
        ordering = ('-create_by',)
        verbose_name = 'Temoignages'
        verbose_name_plural = 'Temoignages'.upper()

    def __str__(self):
        return self.full_name


