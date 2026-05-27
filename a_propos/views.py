from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render

from a_propos.models import AboutUs, Mission, PlusDeStatistiques, Partenaire
from contacts.models import ContactInfo
#from institut_paule_mercure.module_utilitaire import erreur404


class AboutView(View):
    def get(self, request, vue=None):
        print("=========== methode GET ==========", request.GET)
        if vue == 'a_propos':
            return self.aboutUs(request)
        else:
            erreur404()

    def post(self, request):
        # Logique pour gérer les requêtes POST
        # return render(request, 'main/home.html')
        pass

    def aboutUs(self, request):
        about_us = AboutUs.objects.first()  # Assuming there is only one AboutUs entry
        mission_section = Mission.objects.first()
        statistiques = PlusDeStatistiques.objects.first()
        partenaires = Partenaire.objects.all()
        contact_info = ContactInfo.objects.first()
        context = {
        'active_about_us': 'active',
        'about_us': about_us,
        'mission_section': mission_section,
        'statistiques': statistiques,
        'partenaires': partenaires,
        'contact_info': contact_info,
        }
        return render(request, 'templates/a_propos/a_propos.html', context)
