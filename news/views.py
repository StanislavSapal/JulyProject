from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from news.models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from news.utils import MyMixin
from django.contrib import messages
from django.contrib.auth import login, logout


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'sapalstanislav@ukr.net',
                             ['sapals.rozetka@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Емейл відправлено')
                return redirect('test')
            else:
                messages.error(request, 'Помилка відправки')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = ContactForm()
    return render(request, 'news/test.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ви успішно зареєструвались')
            return redirect('home')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm
    return render(request, 'news/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Головна'}
    mixin_prop = 'hello world'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Головна сторінка')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
    raise_exception = False
    # login_url = '/admin/'


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
