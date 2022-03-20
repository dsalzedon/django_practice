from django.urls import path, re_path
from news.views import MainPageView, News

urlpatterns = [
    path("", MainPageView.as_view()),
    re_path("news/(?P<news_link>[^/]*)/?", News.as_view()),
]
