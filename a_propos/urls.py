from django.urls import path
from .views import AboutView

app_name = 'a_propos'

urlpatterns = [
    path('', AboutView.as_view(), {'vue' : 'a_propos'}, name="a_propos"),
]
