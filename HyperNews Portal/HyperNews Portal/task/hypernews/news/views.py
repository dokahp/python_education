from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404
import json
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from datetime import datetime


def redirect_view(request):
    response = redirect('/news/')
    return response


# Create your views here.

class MainPage(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Coming soon')


class CreateNews(View):
    def get(self, request):
        return render(request, 'news/create.html')

    def post(self, request):
        with open(settings.NEWS_JSON_PATH, 'r', encoding='utf-8') as json_file:
            news = json.load(json_file)
        link, title, text = 0, request.POST.get('title'), request.POST.get('text')
        for i in news:
            link = i['link'] + 1
        news.append(
            {'created': datetime.strftime(datetime.today(), '%Y-%m-%d %H:%M:%S'), 'title': title, 'text': text, 'link': link})
        with open(settings.NEWS_JSON_PATH, "w") as json_file:
            json.dump(news, json_file)
        return redirect('/news/')


class NewsPage(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, 'r', encoding='utf-8') as json_file:
            all_articles = json.load(json_file)
        search_articles = []
        try:
            if request.GET.get('q'):
                search = request.GET.get('q')
                for i in all_articles:
                    if search in i['title']:
                        date = i['created']
                        i['created'] = date[0:10]
                        search_articles.append(i)
                search_articles.sort(key=lambda i: i['created'], reverse=True)
                return render(request, 'news/news.html', {'all_articles': search_articles})
            else:
                all_articles.sort(key=lambda i: i['created'], reverse=True)
                for i in all_articles:
                    date = i['created']
                    i['created'] = date[0:10]
                return render(request, 'news/news.html', {'all_articles': all_articles})
        except ValueError:
            return render(request, 'news/news.html', {'all_articles': all_articles})

class ArticlesPage(TemplateView):
    template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = kwargs['article_id']
        context['article_id'] = article_id
        with open(settings.NEWS_JSON_PATH, 'r', encoding='utf-8') as json_file:
            all_articles = json.load(json_file)

        context['text'] = all_articles[article_id - 1]['text']
        context['created'] = all_articles[article_id - 1]['created']
        context['title'] = all_articles[article_id - 1]['title']

        return context
