from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from nos_actions.models import Article
from contacts.models import ContactInfo
from JEFA_main.module_utilitaire import erreur404

class NosActionsView(View):
    def get(self, request, vue=None, tag=None, article_id=None):
        print("=========== methode GET ==========", request.GET)
        if vue == 'nos_actions':
            return self.nosActions(request)
        elif vue == 'articles_list':
            return self.articlesList(request)
        elif vue == 'article_detail' and article_id:
            return self.articleDetail(request, article_id)
        elif vue == 'articles_by_tag' and tag:
            return self.articlesByTag(request, tag)
        else:
            return erreur404(request)

    def nosActions(self, request):
        articles = Article.objects.all().order_by('-date_pub')
        for article in articles:
            print(f"Article: {article.titre}, Image: {article.image}, URL: {article.image.url if article.image else 'No image'}")
        paginator = Paginator(articles, 6)
        page = request.GET.get('page')
        try:
            articles_paginated = paginator.page(page)
        except PageNotAnInteger:
            articles_paginated = paginator.page(1)
        except EmptyPage:
            articles_paginated = paginator.page(paginator.num_pages)

        contact_info = ContactInfo.objects.first()
        context = {
            'active_nos_actions': 'active',
            'articles': articles_paginated,
            'contact_info': contact_info,
        }
        return render(request, 'nos_actions/nos_actions.html', context)

    def articlesList(self, request):
        articles = Article.objects.all().order_by('-date_pub')
        for article in articles:
            print(f"Article: {article.titre}, Image: {article.image}, URL: {article.image.url if article.image else 'No image'}")
        paginator = Paginator(articles, 5)
        page = request.GET.get('page')
        try:
            articles_paginated = paginator.page(page)
        except PageNotAnInteger:
            articles_paginated = paginator.page(1)
        except EmptyPage:
            articles_paginated = paginator.page(paginator.num_pages)

        contact_info = ContactInfo.objects.first()
        context = {
            'active_nos_actions': 'active',
            'articles': articles_paginated,
            'contact_info': contact_info,
        }
        return render(request, 'nos_actions/articles_list.html', context)

    def articleDetail(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        print(f"Article Detail: {article.titre}, Image: {article.image}, URL: {article.image.url if article.image else 'No image'}")
        contact_info = ContactInfo.objects.first()
        context = {
            'active_nos_actions': 'active',
            'article': article,
            'contact_info': contact_info,
        }
        return render(request, 'nos_actions/articles.html', context)

    def articlesByTag(self, request, tag):
        articles = Article.objects.filter(tags__contains=tag).order_by('-date_pub')
        for article in articles:
            print(f"Article: {article.titre}, Image: {article.image}, URL: {article.image.url if article.image else 'No image'}")
        paginator = Paginator(articles, 5)
        page = request.GET.get('page')
        try:
            articles_paginated = paginator.page(page)
        except PageNotAnInteger:
            articles_paginated = paginator.page(1)
        except EmptyPage:
            articles_paginated = paginator.page(paginator.num_pages)

        contact_info = ContactInfo.objects.first()
        context = {
            'active_nos_actions': 'active',
            'articles': articles_paginated,
            'contact_info': contact_info,
            'tag': tag,
        }
        return render(request, 'nos_actions/articles_list.html', context)