# nos_actions/urls.py
from django.urls import path
from .views import NosActionsView

app_name = 'nos_actions'

urlpatterns = [
    path('', NosActionsView.as_view(), {'vue': 'nos_actions'}, name='nos_actions'),
    path('article/', NosActionsView.as_view(), {'vue': 'articles_list'}, name='articles_list'),
    path('article/<int:article_id>/', NosActionsView.as_view(), {'vue': 'article_detail'}, name='article_detail'),
    path('article/tag/<str:tag>/', NosActionsView.as_view(), {'vue': 'articles_by_tag'}, name='articles_by_tag'),
]