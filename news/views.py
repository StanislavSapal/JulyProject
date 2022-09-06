from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from news.models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Головна'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})

# def index(request):
#    news = News.objects.all()
#    context = {
#        'news': news,
#        'title': 'Список новин',
#        }
#    return render(request, 'news/index.html', context)

#def view_news(request, news_id):
    #news_item = News.objects.get(pk=news_id)
#    news_item = get_object_or_404(News, pk=news_id)
#    return render(request, 'news/view_news.html', {'news_item': news_item})


# def add_news(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST)
#        if form.is_valid():
#            # print(form.cleaned_data)
#            # news = News.objects.create(**form.cleaned_data)
#            news = form.save()
#            return redirect(news)
#    else:
#        form = NewsForm()
#    return render(request, 'news/add_news.html', {'form': form})


#def test(request):
#    latest_news = News.objects.filter(title='Новина 1').first()

#    if latest_news:
#        result_title = latest_news.title
#    else:
#        result_title = 'хуй тобі собачій'
#    result = f'<h1>{result_title}</h1>'

#    return HttpResponse(result)

# Cтворити вьюху яка бере саму стару новину. Якшо її тітл не Говно то перейменовує в Говно і веpтає тітл
# Якщо її тітл Говно - пише шо так і було


#def rename_to_govno(request):
#    latest_news = News.objects.all().order_by('-created_at').first()

#    if latest_news.title == 'Говно':
#        result = f'<h2>Заголовок і так був {latest_news.title}</h2>'
#    else:
#        latest_news.title = 'Говно'
#        latest_news.save()
#        result = f'<h2>Вітаємо, заголовок змінено на {latest_news.title}</h2>'

#    return HttpResponse(result)

# Створити вьюху delete_govno яка якшо новинa з тітлом Говно є, то видаляє і пише шо удалила, якшо нема, пише "такої
# новини немає"

#def delete_govno(request):
#    govno_news = News.objects.filter(title='Говно').first()
#
#    if not govno_news:
#        result = f'<h2>Новини з таким заголовком нема, ти шо на приколі? Хто так називає новини?</h2>'
#    else:
#        govno_news_title = govno_news.title
#        govno_news.delete()
#        result = f'<h2>Новину з заголовком {govno_news_title} видалено</h2>'

#    return HttpResponse(result)
