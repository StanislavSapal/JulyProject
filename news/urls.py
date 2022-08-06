from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('test/', test),
    path('rename_latest_news/', rename_to_govno),
    path('delete_govno/', delete_govno)
]