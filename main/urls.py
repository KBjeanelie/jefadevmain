from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from contacts.views import ContactView
from main import views

# Create your views here.
app_name = 'main'

urlpatterns = [
    path("", views.HomeView.as_view(), {'vue': 'home'}, name="home"),
    path("faire_un_don/", views.HomeView.as_view(), {'vue': 'don'}, name="don"),
    path('a_propos/', include('a_propos.urls')),
    path('nos_actions/', include('nos_actions.urls')),
    path('contact/', include('contacts.urls')),
    path('volontariat/', ContactView.as_view(), {'vue': 'volontariat'}, name='volontariat'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
