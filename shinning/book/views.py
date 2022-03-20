from django.views import View
from django.shortcuts import render
from django.views.generic.base import TemplateView


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "book/contents.html", context={"book": book})


class ChapterView(TemplateView):
    template_name = "book/chapter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        n_chapter = kwargs["n_chapter"]
        context["n_chapter"] = n_chapter
        context["content"] = book["Chapter " + n_chapter]
        return context


book = {
    "Chapter 1": "All work and no play makes Jack a dull boy...",
    "Chapter 2": "All work and no play makes Jack a dull boy...",
    "Chapter 3": "All work and no play makes Jack a dull boy...",
    "Chapter 4": "All work and no play makes Jack a dull boy...",
}
