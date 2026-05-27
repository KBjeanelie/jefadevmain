from django.urls import path
from .views import ContactView

app_name = 'contacts'

urlpatterns = [
    path('', ContactView.as_view(), {'vue' : 'contact'}, name='contact'),
    path('save_contact/', ContactView.as_view(), {'vue' : 'save_contact'}, name='save_contact'),
    path('formulaire_volontaire/', ContactView.as_view(), {'vue' : 'formulaire_volontaire'}, name='formulaire_volontaire'),
]
