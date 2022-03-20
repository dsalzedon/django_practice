from django.urls import path, re_path
from candies.views import MainPageView, CandyView

urlpatterns = [
    path("candies/", MainPageView.as_view()),
    re_path("candies/(?P<candy_name>[^/]*)/?", CandyView.as_view()),
]
