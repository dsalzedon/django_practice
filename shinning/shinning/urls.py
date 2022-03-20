from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("contents", book.views.MainPageView.as_view()),
    path("admin/", admin.site.urls),
]
