from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Обрана категорія'}),
         name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('test/', test, name='test')
    # path('', index, name='home'),
    # path('test/', test),
    # path('rename_latest_news/', rename_to_govno),
    # path('delete_govno/', delete_govno, name='delete_govno'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    # path('category/<int:category_id>/', get_category, name='category'),
    # path('news/add-news/', add_news, name='add_news')
]