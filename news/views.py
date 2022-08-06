from django.shortcuts import render
from django.http import HttpResponse

from news.models import News


def index(request):
    #print(request)
    return HttpResponse('<h2>Hello world</h2>')


def test(request):
    latest_news = News.objects.filter(title='Новина 1').first()

    if latest_news:
        result_title = latest_news.title
    else:
        result_title = 'хуй тобі собачій'
    result = f'<h1>{result_title}</h1>'

    return HttpResponse(result)

# Cтворити вьюху яка бере саму стару новину. Якшо її тітл не Говно то перейменовує в Говно і веpтає тітл
# Якщо її тітл Говно - пише шо так і було

def rename_to_govno(request):
    latest_news = News.objects.all().order_by('-created_at').first()

    if latest_news.title == 'Говно':
        result = f'<h2>Заголовок і так був {latest_news.title}</h2>'
    else:
        latest_news.title = 'Говно'
        latest_news.save()
        result = f'<h2>Вітаємо, заголовок змінено на {latest_news.title}</h2>'

    return HttpResponse(result)
# Створити вьюху delete_govno яка якшо новинa з тітлом Говно є, то видаляє і пише шо удалила, якшо нема, пише "такої
# новини немає"

def delete_govno(request):
    wanted_news = News.objects.filter(title='Говно').first()

    if not wanted_news:
        result = f'<h2>Новини з таким заголовком нема, ти шо на приколі? Хто так називає новини?</h2>'
    else:
        wanted_news_title = wanted_news.title
        wanted_news.delete()
        result = f'<h2>Новину з заголовком {wanted_news_title} видалено</h2>'

    return HttpResponse(result)