from django.contrib import admin
from django.urls import path

import main
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', mmain, name='mmain'),
    path('about/', about, name='about'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('search-result/', search_result, name='search-result'),
    path('single-post/', single_post, name='single-post'),
    path('Politics-keyword1/', Politics_keyword1, name='Politics-keyword1'),
]
