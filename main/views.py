from django.views import View
from django.shortcuts import render

from JEFA_main.module_utilitaire import erreur404
from a_propos.models import AboutUs
from contacts.models import ContactInfo
from main.models import CarouselItemBannier, Testimonial
from nos_actions.models import Article

class HomeView(View):
    def get(self, request, vue=None):
        print("=========== methode GET ==========", request.GET)
        if vue == 'home':
            return self.homePage(request)
        elif vue == 'don':
            return self.gestionDon(request)
        else:
            erreur404()

    def post(self, request):
        pass

    def homePage(self, request):
        carousel_items = CarouselItemBannier.objects.all()
        about_us = AboutUs.objects.first()
        testimonials = Testimonial.objects.all()
        contact_info = ContactInfo.objects.first()
        articles = Article.objects.filter(is_favorite=True, date_pub__isnull=False).order_by('-date_pub')[:4]
        context = {
            'active_main': 'active',
            'carousel_items': carousel_items,
            'about_us': about_us,
            'testimonials': testimonials,
            'contact_info': contact_info,
            'articles': articles,
        }
        return render(request, 'main/acceuil.html', context)

    def gestionDon(self, request):
        context = {}
        return render(request, 'main/donation.html', context)