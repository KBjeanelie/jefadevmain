from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

from a_propos.models import Volunteer
from contacts.forms import ContactForm
from contacts.models import ContactInfo
from JEFA_main.module_utilitaire import erreur404, reponseFatal, reponseSucces


class ContactView(View):
    def get(self, request, vue=None):
        print("=========== methode GET ==========", request.GET)
        if vue == 'contact':
            return self.Contacts(request)
        elif vue == 'volontariat':
            return self.Volontariat(request)
        elif vue == 'formulaire_volontaire':
            return self.Volontariat(request)
        else:
            erreur404()

    def post(self, request):
        print("=========== methode POST ==========", request.POST)
        action = request.POST.get('op', None)

        if request.META.get('HTTP_X_REQUESTED_WITH') == "XMLHttpRequest":
            print('La vue ==========', action)

            if action == 'save_contact':
                return JsonResponse(self.enregistrerContactForm(request))

    def Contacts(self, request):
        contact_info = ContactInfo.objects.first()
        context = {
            'active_contact': 'active',
            'contact_info': contact_info,
        }
        return render(request, 'templates/contacts/contacts.html', context)


    def Volontariat(self, request):
        volunteers = Volunteer.objects.all()
        contact_info = ContactInfo.objects.first()
        context = {
            'active_volontariat': 'active',
            'volunteers': volunteers,
            'contact_info': contact_info,
        }
        return render(request, 'templates/contacts/volontariat.html', context)

    def enregistrerContactForm(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # Enregistrer les données dans la base de données
                form.save()

                # Réponse JSON pour l'AJAX
                return reponseSucces('Message envoyé avec succès!')
            else:
                erreurs = '; '.join(
                    f"{champ}: {', '.join(msg_list)}"
                    for champ, msg_list in form.errors.items()
                )
                return reponseFatal(erreurs or 'Veuillez vérifier les champs du formulaire.')

        return reponseFatal({'success': False, 'message': 'Erreur lors de l\'envoi du message.'})


